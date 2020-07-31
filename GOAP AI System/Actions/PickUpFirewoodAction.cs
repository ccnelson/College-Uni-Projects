// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class PickUpFirewoodAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;
	IOrderedEnumerable<SupplyPileComponent> sortedSupplyPiles = null;

	private bool hasFirewood = false;
	private readonly int noOfFirewood = 2;
	
	public PickUpFirewoodAction() 
	{
		addPrecondition ("hasFirewood", false); // don't get firewood if we already have it
		addEffect ("hasFirewood", true); // we now have firewood
	}
	
	
	public override void reset ()
	{
		hasFirewood = false;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return hasFirewood;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to pick up firewood
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
				if (supply.numFirewood >= noOfFirewood)
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
		if (closest.numFirewood >= noOfFirewood)
		{
			closest.numFirewood -= noOfFirewood;
			hasFirewood = true;
			inventory.numFirewood += noOfFirewood;

			return true;
		}  
		else 
		{
			// no firewood available - somedoby got there before us
			return false;
		}
	}
}
