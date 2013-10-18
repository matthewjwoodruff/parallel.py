#New Parallel Coordinate Plots

I've produced new parallel coordinate plots comparing the twenty-seven and eighteen decision variable solution sets.  I'm not sure it works to present the ten-objective sets on the same axes together, because there are so many solutions and it turns into a big purple mess.  I think there's a lot to talk about if we split them up, but that's also quite a lot of real estate.  Another option would be to present the objectives instead of the performance criteria, since we're not planning to lean too hard on recapitulating the MOVA argument.

##A Big Purple Mess

![Both ten objective reference sets together.](ten.png)

Here's what happens when we put the sets together, and make a single parallel coordinate plot. You can see that using twenty-seven decision variables lets us get both better and worse solutions on most axes, although the eighteen decision variable version does worse on VCMAX and LDMAX pretty consistently. But this is a big mess and there's not a lot of info we can get out of it given the amount of ink we're spending on it.

##Clearer With Three Objectives

![The three objective reference sets together.](three.png)

The three-objective formulations don't have that many solutions, so it's a lot easier to see what happens here.  But it's also using up quite a lot of real estate for what it's telling us.

##Separating the Ten Objective Sets

![Just the 27DV set.](twentyseventen.png)

![Just the 18DV set.](eighteenten.png)

If we separate the 27 and 18 decision variable sets, we can see significantly better solutions for ROUGH, WEMP, WFUEL, and RANGE when we use 27 decision varaibles.  But now we're spending a whole page to a page and a half, just on parallel coordinate plots.

##Using Only Objectives

![27DV --- ten objectives](twentyseventen_objectives.png)

![18DV --- ten objectives](eighteenten_objectives.png)

![Three objectives](three_objectives.png)

This is my preference.  Since we're talking about hypervolume, which is computed in objective space, throughout the rest of the results section, I think this provides the clearest picture of how the number of decision variables in the problem formulation affects what we're actually measuring.  We might also be able to get away with combining the sets if we stretch the axes a bit:

![27 and 18 DV together with stretched axes.](ten_objectives.png)


