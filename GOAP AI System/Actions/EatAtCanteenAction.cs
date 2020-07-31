// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class EatAtCanteenAction : GoapAction
{
	private CanteenComponent[] canteens = null;
	private IOrderedEnumerable<CanteenComponent> orderedCanteens = null;
	private CanteenComponent closest = null;

	private bool eaten = false;
	private float startTime = 0f;
	private readonly float eatDuration = 4f;
	private readonly int foodConsumed = 1;
	private readonly int energyGained = 5;
	

	public EatAtCanteenAction() 
	{
		addPrecondition ("isHungry", true); // agent energy is <= 0
		addPrecondition("hasFood", true); // agent has collected food to eat
		addEffect ("isHungry", false); // agent no longer hungry
	}
	
	public override void reset ()
	{
		eaten = false;
		startTime = 0;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return eaten;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to collect food
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (canteens == null)
		{
			canteens = FindObjectsOfType(typeof(CanteenComponent)) as CanteenComponent[];
		}

		if (orderedCanteens == null)
		{
			orderedCanteens = canteens.OrderBy(t => Vector3.Distance(transform.position, t.transform.position));
		}

		foreach (CanteenComponent canteen in orderedCanteens)
		{
			if (canteen.engaged == false)
			{
				closest = canteen;
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
		// although precondition check ensures canteen isnt engaged,
		// this status may have changed whilst walking to canteen

		if (startTime == 0 && closest.engaged != true)
		{
			startTime = Time.time;
			closest.engaged = true;
			if (!eaten) { animator.SetTrigger("smoke"); }
		}
		else if (startTime == 0 && closest.engaged == true)
		{
			return false;
		}
			
		if (Time.time - startTime > eatDuration)
		{
			eaten = true;
			closest.engaged = false;
			animator.ResetTrigger("smoke"); // smoke animation resembles eating
			inventory.energy += energyGained;
			inventory.numFood -= foodConsumed;
		}
		return true;
	}
}
