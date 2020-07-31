// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class DrinkFromWellAction : GoapAction
{
	private WellComponent[] wells = null;
	private IOrderedEnumerable<WellComponent> orderedWells = null;
	private WellComponent closest = null;

	private bool drunk = false;
	private float startTime = 0f;
	private float drinkDuration = 3f;
	private int hydrationAmount = 5;
	
	public DrinkFromWellAction() 
	{
		addPrecondition ("isThirsty", true); // don't drink if not thirsty
		addEffect ("isThirsty", false); // now hydrated
	}
	
	public override void reset ()
	{
		drunk = false;
		closest = null;
		startTime = 0;
	}
	
	public override bool isDone ()
	{
		return drunk;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a well
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (wells == null)
		{
			wells = FindObjectsOfType(typeof(WellComponent)) as WellComponent[];
		}

		if (orderedWells == null)
		{
			orderedWells = wells.OrderBy(t => Vector3.Distance(transform.position, t.transform.position));
		}

		foreach (WellComponent well in orderedWells)
		{
			if (well.engaged == false)
			{
				closest = well;
				break;
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
		if (startTime == 0 && closest.engaged != true)
		{
			startTime = Time.time;
			closest.engaged = true;
			if (!drunk) { animator.SetTrigger("smoke"); }  // smoking resembles consumption
		}
		else if (startTime == 0 && closest.engaged == true)
		{
			return false;
		}
			
		if (Time.time - startTime > drinkDuration)
		{
			closest.engaged = false;
			inventory.hydration += hydrationAmount;
			drunk = true;
			animator.ResetTrigger("smoke");
		}
		return true;

	}
}
