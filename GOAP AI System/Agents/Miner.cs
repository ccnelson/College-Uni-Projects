// C NELSON UoH 2020
// Agent class implementing Labourer abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using UnityEngine;
using System.Collections.Generic;

public class Miner : Labourer
{
	/**
	 * Our only goal will ever be to mine ore.
	 * The MineOreAction will be able to fulfill this goal.
	 */
	public override HashSet<KeyValuePair<string,object>> createGoalState () 
	{
		HashSet<KeyValuePair<string,object>> goal = new HashSet<KeyValuePair<string,object>> ();
		
		goal.Add(new KeyValuePair<string, object>("minerGoal", true ));
		return goal;
	}

	private void Awake()
	{
		// load reference to required tool
		inventory.toolPrefab = (GameObject)Resources.Load("Equipped Pick", typeof(GameObject));
	}
}

