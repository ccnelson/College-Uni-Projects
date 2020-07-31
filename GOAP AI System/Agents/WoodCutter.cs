// C NELSON UoH 2020
// Agent class implementing Labourer abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using UnityEngine;
using System.Collections.Generic;

public class WoodCutter : Labourer
{
	/**
	 * Our only goal will ever be to chop logs.
	 * The ChopFirewoodAction will fulfill this goal.
	 */
	public override HashSet<KeyValuePair<string,object>> createGoalState () 
	{
		HashSet<KeyValuePair<string,object>> goal = new HashSet<KeyValuePair<string,object>> ();
		
		goal.Add(new KeyValuePair<string, object>("woodcutterGoal", true ));
		return goal;
	}

	private void Awake()
	{
		// load reference to required tool
		inventory.toolPrefab = (GameObject)Resources.Load("Equipped Axe", typeof(GameObject));
	}
}

