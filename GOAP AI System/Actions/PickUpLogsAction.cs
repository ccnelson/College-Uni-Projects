// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class PickUpLogsAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;
	IOrderedEnumerable<SupplyPileComponent> sortedSupplyPiles =  null;

	private bool hasLogs = false;
	private readonly int noOfLogs = 2;
	
	public PickUpLogsAction () 
	{
		addPrecondition ("hasLogs", false); // don't get logs if we already have some
		addEffect ("hasLogs", true); // we now have logs
	}
	
	
	public override void reset ()
	{
		hasLogs = false;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return hasLogs;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to pick up logs
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (supplyPiles == null)
		{
			supplyPiles = FindObjectsOfType(typeof(SupplyPileComponent)) as SupplyPileComponent[];
		}

		if (sortedSupplyPiles == null)
		{
			sortedSupplyPiles = supplyPiles.OrderBy(t => Vector3.Distance(transform.position, t.transform.position));
		}

		if (closest == null)
		{
			foreach (SupplyPileComponent supply in sortedSupplyPiles)
			{
				if (supply.numLogs >= noOfLogs)
				{
					closest = supply;
					break;
				}
			}
		}

		if (closest != null)
		{
			target = closest.gameObject;
		}

		return closest != null;
	}
	
	public override bool perform (GameObject agent)
	{
		if (closest.numLogs >= noOfLogs) 
		{
			closest.numLogs -= noOfLogs;
			hasLogs = true;
			inventory.numLogs += noOfLogs;
			
			return true;
		} 
		else 
		{
			// supply ran out before agent arrived
			return false;
		}
	}
}

