// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using UnityEngine;

public class WanderAction : GoapAction
{
	private GameObject destination = null; // represent destination as object

	private bool wandered = false;
	private float startTime = 0f;
	private int wanderDuration = 15;

	public WanderAction()
	{
		addPrecondition("isNight", false); // no night wandering
		addEffect ("hasWandered", true); // we wandered
		addEffect("peasantGoal", true); // wandering is peasants only goal

		// adding wander as a precondition
		// will cause agent to wander during routine
	}

	public override void reset ()
	{
		wandered = false;
		startTime = 0f;
}
	
	public override bool isDone ()
	{
		return wandered;
	}
	
	public override bool requiresInRange ()
	{
		return true;
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		//  create object
		if (destination == null)
		{
			 destination = new GameObject();
		}
		// give object random but accessible position
		destination.transform.SetPositionAndRotation(RandomNavmeshPosition(transform.position, 10f, -1), transform.rotation);
		// return object as target
		target = destination.gameObject;

		return true;
	}

	public override bool perform(GameObject agent)
	{
		if (startTime == 0)
		{
			startTime = Time.time;
		}

		if (Time.time - startTime > wanderDuration)
		{
			// already moved via target sent in checkProceduralPrecondition	
			inventory.energy -= inventory.MoodModifier(energyConsumed);
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			wandered = true;
		}
		return true;
	}
}
