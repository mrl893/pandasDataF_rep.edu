
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

get_ipython().run_line_magic('matplotlib', 'inline')





print('python version' + sys.version)
print('pandas version:' + pd.__version__)
print('matplotlib version' + matplotlib.__version__)


# We will be creating our own test data for analysis.



# set seed
np.seed(111)

# Function to generate test data
def CreateDataSet(Number=1):

    Output = []

    for i in range(Number):

        # Create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25,high=1000,size=len(rng))

        # Status pool
        status = [1,2,3]

        # Make a random list of statuses
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['GA','FL','fl','NY','NJ','TX']

        # Make a random list of states
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output




dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
df.info()





df.head(10)




# Save results to excel
df.to_excel('Lesson3.xlsx', index=False)
print('Done')



get_ipython().run_line_magic('pinfo', 'pd.read_excel')





# Location of file
Location = r'C:\Users\master\Desktop\Lesson3.xlsx'

# Parse a specific sheet
df = pd.read_excel(Location, 0, index_col='StatusDate')
df.dtypes


# In[9]:


df.index


# In[10]:


df.head()


# #Prepare Data
# This section attempts to clean up the data for analysis.
#
# Make sure the state column is all in upper case
# Only select records where the account status is equal to "1"
# Merge (NJ and NY) to NY in the state column
# Remove any outliers (any odd results in the data set)

# In[11]:


df['State'].unique()


# In[12]:


# Clean State Column, convert to upper case
df['State'] = df.State.apply(lambda x: x.upper())


# In[13]:


df['State'].unique()


# In[14]:


# Only grab where Status == 1
mask = df['Status'] == 1
df = df[mask]


# In[15]:


# Convert NJ to NY
mask = df.State == 'NJ'
df['State'][mask] = 'NY'


# In[16]:


df['State'].unique()


# In[17]:


df['CustomerCount'].plot(figsize=(15,5));


# If we take a look at the data, we begin to realize that there are multiple values for the same State, StatusDate, and Status combination. It is possible that this means the data you are working with is dirty/bad/inaccurate, but we will assume otherwise. We can assume this data set is a subset of a bigger data set and if we simply add the values in the CustomerCount column per State, StatusDate, and Status we will get the Total Customer Count per day.

# In[18]:


sortdf = df[df['State']=='NY'].sort_index(axis=0)
sortdf.head(10)


# Our task is now to create a new dataframe that compresses the data so we have daily customer counts per State and StatusDate. We can ignore the Status column since all the values in this column are of value 1. To accomplish this we will use the dataframe's functions groupby and sum().
#
# Note that we had to use reset_index . If we did not, we would not have been able to group by both the State and the StatusDate since the groupby function expects only columns as inputs. The reset_index function will bring the index StatusDate back to a column in the dataframe.

# In[19]:


# Group by State and StatusDate
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
Daily.head()


# The State and StatusDate columns are automatically placed in the index of the Daily dataframe. You can think of the index as the primary key of a database table but without the constraint of having unique values. Columns in the index as you will see allow us to easily select, plot, and perform calculations on the data.
#
# Below we delete the Status column since it is all equal to one and no longer necessary.

# In[20]:


del Daily['Status']
Daily.head()


# In[21]:


# What is the index of the dataframe
Daily.index


# In[22]:


# Select the State index
Daily.index.levels[0]


# In[23]:


# Select the StatusDate index
Daily.index.levels[1]


# Lets now plot the data per State.
#
# As you can see by breaking the graph up by the State column we have a much clearer picture on how the data looks like. Can you spot any outliers?

# In[24]:


Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot();


# We can also just plot the data on a specific date, like 2012. We can now clearly see that the data for these states is all over the place. since the data consist of weekly customer counts, the variability of the data seems suspect. For this tutorial we will assume bad data and proceed.

# In[25]:


Daily.loc['FL']['2012':].plot()
Daily.loc['GA']['2012':].plot()
Daily.loc['NY']['2012':].plot()
Daily.loc['TX']['2012':].plot();


# We will assume that per month the customer count should remain relatively steady. Any data outside a specific range in that month will be removed from the data set. The final result should have smooth graphs with no spikes.
#
# StateYearMonth - Here we group by State, Year of StatusDate, and Month of StatusDate.
# Daily['Outlier'] - A boolean (True or False) value letting us know if the value in the CustomerCount column is ouside the acceptable range.
#
# We will be using the attribute transform instead of apply. The reason is that transform will keep the shape(# of rows and columns) of the dataframe the same and apply will not. By looking at the previous graphs, we can realize they are not resembling a gaussian distribution, this means we cannot use summary statistics like the mean and stDev. We use percentiles instead. Note that we run the risk of eliminating good data.

# In[26]:


# Calculate Outliers
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])

# Remove Outliers
Daily = Daily[Daily['Outlier'] == False]


# The dataframe named Daily will hold customer counts that have been aggregated per day. The original data (df) has multiple records per day. We are left with a data set that is indexed by both the state and the StatusDate. The Outlier column should be equal to False signifying that the record is not an outlier.

# In[27]:


Daily.head()


# We create a separate dataframe named ALL which groups the Daily dataframe by StatusDate. We are essentially getting rid of the State column. The Max column represents the maximum customer count per month. The Max column is used to smooth out the graph

# In[28]:


# Combine all markets

# Get the max customer count by Date
ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount'] # rename column

# Group by Year and Month
YearMonth = ALL.groupby([lambda x: x.year, lambda x: x.month])

# What is the max customer count per Year and Month
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())
ALL.head()


# As you can see from the ALL dataframe above, in the month of January 2009, the maximum customer count was 901. If we had used apply, we would have got a dataframe with (Year and Month) as the index and just the Max column with the value of 901.
#
# There is also an interest to gauge if the current customer counts were reaching certain goals the company had established. The task here is to visually show if the current customer counts are meeting the goals listed below. We will call the goals BHAG (Big Hairy Annual Goal).
#
# 12/31/2011 - 1,000 customers
# 12/31/2012 - 2,000 customers
# 12/31/2013 - 3,000 customers
# We will be using the date_range function to create our dates.
#
# Definition: date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False, name=None, closed=None)
# Docstring: Return a fixed frequency datetime index, with day (calendar) as the default frequency
#
# By choosing the frequency to be A or annual we will be able to get the three target dates from above.

# In[29]:


get_ipython().run_line_magic('pinfo', 'pd.date_range')


# In[30]:


# Create the BHAG dataframe
data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=['BHAG'])
BHAG


# In[31]:


# Combine the BHAG and the ALL data set
combined = pd.concat([ALL,BHAG], axis=0)
combined = combined.sort_index(axis=0)
combined.tail()


# In[32]:


ig, axes = plt.subplots(figsize=(12, 7))

combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best');


# There was also a need to forecast next year's customer count and we can do this in a couple of simple steps. We will first group the combined dataframe by Year and place the maximum customer count for that year. This will give us one row per Year.

# In[33]:


# Group by Year and then get the max value per year
Year = combined.groupby(lambda x: x.year).max()
Year


# In[34]:


# Add a column representing the percent change per year
Year['YR_PCT_Change'] = Year['Max'].pct_change(periods=1)
Year


# In[35]:


(1 + Year.loc[2012,'YR_PCT_Change']) * Year.loc[2012,'Max']


# Present Data¶
# Create individual Graphs per State.

# In[36]:


# First Graph
ALL['Max'].plot(figsize=(10, 5));plt.title('ALL Markets')

# Last four Graphs
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
fig.subplots_adjust(hspace=1.0) ## Create space between plots

Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,1])
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,0])
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,1])

# Add titles
axes[0,0].set_title('Florida')
axes[0,1].set_title('Georgia')
axes[1,0].set_title('Texas')
axes[1,1].set_title('North East');


# In[ ]:
