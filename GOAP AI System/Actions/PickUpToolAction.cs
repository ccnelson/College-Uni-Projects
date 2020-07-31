// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class PickUpToolAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;
	IOrderedEnumerable<SupplyPileComponent> sortedSupplyPiles = null;

	private bool hasTool = false;
	private readonly int noOfTools = 1;

	public PickUpToolAction () 
	{
		addPrecondition ("hasTool", false); // don't get a tool if we already have one
		addEffect ("hasTool", true); // we now have a tool
	}

	public override void reset ()
	{
		hasTool = false;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return hasTool;
	}

	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to pick up a tool
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
				if (supply.numTools >= noOfTools)
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
		if (closest.numTools >= noOfTools)
		{
			closest.numTools -= noOfTools;
			hasTool = true;

			// create the tool and add it to the agent
			inventory.tool = Instantiate(inventory.toolPrefab, inventory.handTransform);

			return true;
		} 
		else 
		{
			// no tool available, supply ran out before agent arrived
			return false;
		}
	}

}


