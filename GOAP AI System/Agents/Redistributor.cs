// C NELSON UoH 2020
// Agent class implementing Labourer abstract class

using System.Collections.Generic;

public class Redistributor : Labourer
{

	public override HashSet<KeyValuePair<string,object>> createGoalState () 
	{
		HashSet<KeyValuePair<string,object>> goal = new HashSet<KeyValuePair<string,object>> ();
		
		goal.Add(new KeyValuePair<string, object>("redistributorGoal", true ));
		return goal;
	}

}

