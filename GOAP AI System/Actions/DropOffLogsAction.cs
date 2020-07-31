// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class DropOffLogsAction: GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;

	private bool droppedOffLogs = false;
	
	public DropOffLogsAction () 
	{
		addPrecondition ("hasLogs", true); // can't drop off logs if we don't already have some
		addEffect ("hasLogs", false); // we now have no logs
		addEffect ("loggerGoal", true); // delivered logs
	}
	
	public override void reset ()
	{
		droppedOffLogs = false;
	}
	
	public override bool isDone ()
	{
		return droppedOffLogs;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to drop off logs
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
		//if (inventory.numLogs <= 0)
		//{
		//	return false;
		//}
		
		closest.numLogs += inventory.numLogs;
		droppedOffLogs = true;
		inventory.numLogs = 0;
		
		return true;
	}
}
