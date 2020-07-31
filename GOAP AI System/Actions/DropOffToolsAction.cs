// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class DropOffToolsAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;

	private bool droppedOffTools = false;
	private readonly int noOfTools = 2;
	
	public DropOffToolsAction () 
	{
		addPrecondition ("hasNewTools", true); // need new tools to drop off
		addEffect ("hasNewTools", false); // now have no tools
		addEffect("blacksmithGoal", true); // we delivered tools

		// hasNewTools effect occurs as result of forge tools,
		// blacksmith and cook are unique in this sense. nothing is removed from inventory
		// when delivering tools. 
		// blacksmith is the only agent to ever have newtools.
		// Instead of adding it as an inventory item it is 
		// tracked by the planner as a prerequisite.
		// cook uses a similar approach to track newly cooked food.
		// this prevents confusion between regular tools, and newly created tools.
	}

	public override void reset ()
	{
		droppedOffTools = false;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return droppedOffTools;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near supply pile
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (supplyPiles == null)
		{
			supplyPiles = FindObjectsOfType(typeof(SupplyPileComponent)) as SupplyPileComponent[];
		}

		if (closest == null)
		{
			closest = supplyPiles.OrderBy(t => Vector3.Distance(transform.position, t.transform.position)).FirstOrDefault();
		}

		if (closest != null)
		{
			target = closest.gameObject;
		}

		return closest != null;
	}
	
	public override bool perform (GameObject agent)
	{
		closest.numTools += noOfTools;
		droppedOffTools = true;
		
		return true;
	}
}