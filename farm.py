import statistics as stats
import functions as functions

class Cuerdas:
    
    # currently the program runs by iterating through a list where each tree is its own value (an integrer representing its age). I think that this approach offers benefits for later when we implement probabilities with trees sporadically dying from rust and CBB. I also think it allows for much easier access to information like: how many trees are in production; what is the average age of the trees in this plot (otherwise you need to weight the averages) it also allows us to have many different aged trees. It's logical! But it's slow as hell.
    
    # I'm wondering if a middle ground would be to break the trees up into like micro-plots of 50-100 trees, so we could have the same benefits but not have to iterate through so many objects.
    
    # Not sure how we will proceed. But it works, and I'm happy about that!
    
    def __init__(self, _farmerName, _cuerdas, _treeType, _initialAgeOfTrees, _sowDensity = functions.hectaresToCuerdas(1000)): # use self to declare namespace
        """
        
        Parameters
        ----------
        
        _cuerdass : int or float
            `_cuerdas` is the number of cuerdas (of a specific tree type, see _treeType)
            
        _initialAgeOfTrees: int or float
            the age of these trees, where 0 is the age at which they were transplanted (generally as small seedlings/saplings). 
            
            float values can be passed, but the program will automatically round and convert to an integer, so int is preferred
        
        _sowDensity : int
            `_sowDensity` refers to the density of trees per cuerda. The standard, expected unit for this initializer is
            trees-per-cuerda. however, units can be converted
        
        
        """
        
        self.farmerName = _farmerName
        
        self.inheretTreeProperties(_treeType)
        
        self.totalCuerdas = _cuerdas
        self.sowDensity = _sowDensity # sow density in trees/hectare
        self.totalTrees = int(round((_cuerdas * _sowDensity), 0)) # round to nearest and convert to int because we can't have poritions of trees
        # and it needs to be an int to iterate through
        
        # adjust the initial age of trees to be a round number
        
        self.initialAgeOfTrees = self.convertToRoundInt(_initialAgeOfTrees)
        
        #self.numOfTrees = _cuerdas * _sowDensity # how many [insert tree name] there are
        self.trees = [self.initialAgeOfTrees for i in range(self.totalTrees)]
        
        self.averageAgeOfTrees = stats.mean(self.trees)
        
        
        self.harvestPerTree = self.cuerdaHarvestCap / _sowDensity # pull initial sow density because the other will change
        # if plants are added or if others die
        self.totalHarvest = 0 # units, in this case pounds
        
        
        
        # initialize variables for pruning so if/else can deal with objects
        self.pruneYear = False
        self.pruneCount = 0
        
    def inheretTreeProperties(self, treeType):
        loop = True
        """
        Based on the argument treeType in the initializer function, assign parameters for the respective
        life & production patterns of the trees on the cuerda.
        
        The following property assignments were developed from data collected from the co-op in 2014
    
        """
        while loop:
            if (treeType =='borbon'):
                self.firstHarvest = {'year': 4, 'proportion': 0.2} # year of first harvest and proportion of harvest until full
                self.fullHarvest = {'year': 5, 'proportion': 1.0}  # year of first harvest and proportion of harvest
                self.descentHarvest = {'year': 28, 'proportionDescent': 0.2} # year that production descends and annual proportion descent
                # self.pruneHarvest = {'yearShift': -5, 'proportionAscent': 0.2} # these are placeholder values to remember to add member val
                self.death = {'year': 30} # year in which trees are expelled from dataset

                self.cuerdaHarvestCap = 200 # units, in this case lbs, per cuerda
                self.treeType = 'borbon'

                loop = False
                
                
            elif (treeType =='catuaí') or (treeType == 'catuai'):
                self.firstHarvest = {'year': 3, 'proportion': 0.2} # year of first harvest and proportion of harvest until full
                self.fullHarvest = {'year': 4, 'proportion': 1.0}  # year of first harvest and proportion of harvest
                self.descentHarvest = {'year': 15, 'proportionDescent': 0.2} # year that production descends and annual proportion descent
                # self.pruneHarvest = {'yearShift': -5, 'proportionAscent': 0.2} # these are placeholder values to remember to add member val
                self.death = {'year': 17} # year in which trees are expelled from dataset

                self.cuerdaHarvestCap = 125 # units, in this case lbs, per cuerda
                self.treeType = 'catuai'

                loop = False

            elif (treeType == 'e14') or (treeType == 'E14'):
                self.firstHarvest = {'year': 4, 'proportion': 0.2} # year of first harvest and proportion of harvest until full
                self.fullHarvest = {'year': 5, 'proportion': 1.0}  # year of first harvest and proportion of harvest
                self.descentHarvest = {'year': 13, 'proportionDescent': 0.2} # year that production descends and annual proportion descent
                # self.pruneHarvest = {'yearShift': -5, 'proportionAscent': 0.2} # these are placeholder values to remember to add member val
                self.death = {'year': 15} # year in which trees are expelled from dataset

                self.cuerdaHarvestCap = 125 # units, in this case lbs, per cuerda
                self.treeType = 'e14'
                
                loop = False

            elif (treeType == 'caturra') or (treeType == 'catura'):
                self.firstHarvest = {'year': 3, 'proportion': 0.2} # year of first harvest and proportion of harvest until full
                self.fullHarvest = {'year': 4, 'proportion': 1.0}  # year of first harvest and proportion of harvest
                self.descentHarvest = {'year': 14, 'proportionDescent': 0.2} # year that production descends and annual proportion descent
                # self.pruneHarvest = {'yearShift': -5, 'proportionAscent': 0.2} # these are placeholder values to remember to add member val
                self.death = {'year': 16} # year in which trees are expelled from dataset

                self.cuerdaHarvestCap = 125 # units, in this case lbs, per cuerda
                self.treeType = 'caturra'

                loop = False

            else: # uncomplete option
                choice01 = ("This tree species does not exist. Would you like to (0) re-elect a tree type or (1) make a new tree type: ")
                if (choice01 == 0) or (choice01 == False):
                    print("some stuff")
                            
                elif (choice01 == 1) or (choice01 == True):
                    print("some other stuff")
                    
                loop = False
                                         
                                         
    def convertToRoundInt(self, number): 
        """
        
        A function to assure that specific numbers in the class are rounded and/or converted to type: int
        
        Parameters
        ----------
        
        number : int, float, or str
            depending on the variable type, takes a route that converts it to a round number of type int
        
        """
                                         
        if type(number) == int:
            final = number
        elif type(number) == float:
            final = int(round(number, 0))
        elif type(number) == str:
            temp = float(number)
            final = round(temp, 0)
        else:
            print("Invalid data type")
                        
        return(final)

        
    def addTreesAuto(self, numTrees, ages = 0): 
        """
        Automatically adds trees to existing cuerdas. Possible implications are intercropping between existing
        trees/rows.
        
        Note: this function will adjust the average age of trees, thesow/plant density, 
        and the total # of trees stored in self.averageAgeOfTrees, self.sowDensity, and self.totalTrees 
        
        Parameters
        ----------
        self : class
            required to change-by-reference members of the class
            
        number: int
            the number of trees the user will add to the set
            
        ages : int
            the age of the trees (which translates to the element in the list)
            the user will add to the set. default value is 0 because most
            trees are planted/added as seeds/saplings, however the param
            is adjustable because it might be useful if adding new land with
            existing trees.
            
        """
                        
        ages = self.convertToRoundInt(ages)
        numTrees = self.convertToRoundInt(numTrees) # even though you can't have portions of a tree, you never know
                        
        for i in range(len(number)):
            self.trees.append(ages) # all trees planted begin at age 0
            
        self.totalTrees += numTrees
        self.sowDensity = self.totalTrees * cuerdas
        self.averageAgeOfTrees = stats.mean(self.trees)
            
    def addTreeSet(self, ls): # adds trees to existing cuerdas
        """
        
        Adds trees to existing cuerdas with a list of ages. Possible implications are intercropping between existing
        trees/rows.
        
        Note: this function will adjust the average age of trees, thesow/plant density, 
        and the total # of trees stored in self.averageAgeOfTrees, self.sowDensity, and self.totalTrees 
        
        Parameters
        ----------
        self : class
            required to change-by-reference members of the class
            
        ls : list
            a list (of int) where each element represents a 'tree,' with
            the element's value representing that specific tree's age
            
        see also:
            makeTreesFromLand
            
        """
        numTrees = len(ls)
        
        for i,e in enumerate(ls):
            age = self.convertToRoundInt(e)
            self.trees.append(age)
            
        self.totalTrees += numTrees
        self.sowDensity = self.totalTrees * cuerdas
        self.averageAgeOfTrees = stats.mean(self.trees)
            
    # this may be a subfunciton in the 'addYears' function
    
    def addCuerdas(self, cuerdas, ageOfTrees, treesPerCuerda = 2750):
        # assign new variables to avoid confusion
        # if user wants to add land without trees, set treesPerCuerda to zero (note: other variables in the class
        # will reflect this change)
        oldSowDens = self.sowDensity
        oldCuerdas = self.totalCuerdas
        newCuerdas = self.totalCuerdas + cuerdas
        
        self.sowDensity = (treesPerCuerda * (cuerdas / newCuerdas)) + (oldSowDens * (oldCuerdas / newCuerdas))
        # calculate weighted avg and push new value to self.treesPerCuerda
        
        # acually update total cuerdas after to avoid confusion
        self.totalCuerdas += cuerdas
        
                        
        ageOfTrees = self.convertToRoundInt(ageOfTrees) 
                        
        # append the new trees to the
        numTrees = self.convertToRoundInt(cuerdas * treesPerCuerda) # assure number of trees is iterable
                        
        for i in range(len(numTrees)):
            self.trees.append(ageOfTrees)
            
        self.totalTrees += numTrees
        self.averageAgeOfTrees = stats.mean(self.trees)
        
    
    def setPruneTrees(self):
        """
        Takes in `pruneYear` bool, sets self.pruneYear to equiveleant value. 
        
        """
        self.pruneYear = True
        
        # how much the total yield will increase after trees grow back from pruning (i.e. after pruneCount years)
        self.pruneGrowth = 0.10 
        
        # current yield - (current yield * (this proportion * countyear)) = yield for that year.
        self.pruneDelay = 0.20
        # caution! The product of this proportion ^^^ and count year SHANT EXCEED 1.0 otherwise the 
        # program will simulate impossibilities
        
        if pruneYear == True: # the if-else is set up in case the main function decides to pass this on ever iteration
            self.pruneCount = 3
            
            # increase total yield-per-tree to 10% higher
            self.harvestPerTree = self.harvestPerTree + (self.pruneGrowth * self.harvestPerTree)
            
        
    def oneYear(self):
        """
        
        This function takes this entire set of trees and adjusts the member values in the class to grow/change/produce accordingly.
        The function uses preset parameters for the specific tree type to guide the flow-control.
        
        """
        for treeIndex, treeAge in enumerate(self.trees):
            if (self.pruneYear == True):
                # make sure to:
                # (1) still age the trees
                # (2) make them produce less for a bit!? How!?
                # (3) increase total production or lifespan long-term
                
                self.trees[treeIndex] += 1 # trees still age when they're pruned
                self.pruneCount -= 1 # lower the countdown to full yield by one year
                
                self.pruneYear = False # it is no longer a prune year and so this shifts it back to cycle
                
            elif (self.pruneCount > 0):
                
                subtract = self.pruneDelay * self.pruneCount
                
                if (subtract > 1.0):
                    break
                    print("Impossible proportion as a result of pruneCount and pruneDelay.")
                    print("Please assure product of pruneCount and pruneDelay is always <= 1.0")
                
                product = self.harvestPerTree - (self.harvestPerTree * (subtract))
            
                self.trees[treeIndex] += 1 # trees still age when they're pruned
                self.pruneCount -= 1 # lower the countdown to full yield by one year
            
            elif (treeAge < self.firstHarvest['year']):
                
                
                # product = 0 #in this range the trees produce nothing, but they still move up in age for the year
                # self.totalHarvest += product
                self.trees[treeIndex] += 1
                
                
            elif (treeAge >= self.firstHarvest['year']) and (treeAge < self.fullHarvest['year']):
                
                product = self.harvestPerTree * self.firstHarvest['proportion']
                self.totalHarvest += product
                self.trees[treeIndex] += 1 # assure to reference the list and not the copy
                
                
            elif ((treeAge >= self.fullHarvest['year']) and (treeAge < self.descentHarvest['year'])):
                
                product = self.harvestPerTree * self.fullHarvest['proportion']
                self.totalHarvest += product
                self.trees[treeIndex] += 1
                
                
            elif ((treeAge >= self.descentHarvest['year']) and (treeAge < self.death['year'])):
                
                yearsIntoDescent = treeAge - self.descentHarvest['year']
                proportion = self.fullHarvest['proportion'] - (yearsIntoDescent * self.descentHarvest['proportionDescent'])
                product = self.harvestPerTree * proportion
                self.totalHarvest += product
                self.trees[treeIndex] += 1
                
                
            elif (treeAge == self.death['year']):
                self.trees[treeIndex] += 1
                continue
            
                
            elif (treeAge >= (self.death['year'] + 1)):
                # if it is the year after the tree died...
                self.trees[treeIndex] = 0 # plant a new tree
                
            else:
                print("""The number: %d, list index: %d is out of range:
                a tree can not be less than 0 years old, and a tree of this type can not be more than
                %d years of age"""%(treeAge, treeIndex, self.death['year']))
                break
                   
        #self.trees[:] = [age for age in self.trees if (age < self.death['year'])] # call-by-reference overwrite of ls removing dead trees. 
        # assure this ^ is outside of the loop & assure the list references the full index with '[:]'
        livingTrees = [age for age in self.trees if (age < self.death['year'])]
        self.totalTrees = len(livingTrees)
                  
        if self.totalTrees > 0:
            self.averageAgeOfTrees = stats.mean(self.trees)
            self.sowDensity = self.totalTrees / self.totalCuerdas
        
            
    def getHarvest(self):
        """
        
        return the total harvest
        
        """
        return(self.totalHarvest)
    
    def setHarvestZero(self):
        """
        
        You must set Harvest to zero after each iteration of oneYear if you want to keep track of annual production
        as opposed to total time production
        
        """
        self.totalHarvest = 0
        
        
        
