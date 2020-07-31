// C NELSON UoH 2020
// Agent class implementing Labourer abstract class

using UnityEngine;
using System.Collections.Generic;

public class Cook : Labourer
{

	public override HashSet<KeyValuePair<string,object>> createGoalState () 
	{
		HashSet<KeyValuePair<string,object>> goal = new HashSet<KeyValuePair<string,object>> ();
		
		goal.Add(new KeyValuePair<string, object>("cookGoal", true ));
		return goal;
	}

	private void Awake()
	{
		// load reference to required tool
		inventory.toolPrefab = (GameObject)Resources.Load("Equipped Knife", typeof(GameObject));
	}
}

