// C NELSON UoH 2020
// Labourer abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using UnityEngine;
using System.Collections.Generic;
using UnityEngine.AI;
using TMPro;


/**
 * A general labourer class.
 * You should subclass this for specific Labourer classes and implement
 * the createGoalState() method that will populate the goal for the GOAP
 * planner.
 */
public abstract class Labourer : MonoBehaviour, IGoap
{
	public InventoryComponent inventory;
	public NavMeshAgent navmesh;
	public TextMeshPro text;
	private Animator animator = null;

	private bool startingMovement = false;
	private readonly float distanceToReach = 1f;

	// default navmesh values
	private readonly int navspeed = 3;
	private readonly int acceleration = 2;
	private readonly float stoppingDistance = 0.1f;



	private void Start()
	{
		navmesh = GetComponent<NavMeshAgent>(); // get navmesh
		text = GetComponentInChildren<TextMeshPro>(); // get text
		animator = GetComponentInChildren<Animator>(); // get animator
		// a handcomponent is assigned to the models Right_Hand_jnt
		inventory.handTransform = GetComponentInChildren<HandComponent>().transform;

		// instantiate tool
		if (inventory.tool == null && inventory.toolPrefab != null)
		{
			inventory.tool = Instantiate(inventory.toolPrefab, inventory.handTransform);
		}

	}

	/**
	 * Key-Value data that will feed the GOAP actions and system while planning.
	 */
	public HashSet<KeyValuePair<string,object>> getWorldState () {
		HashSet<KeyValuePair<string,object>> worldData = new HashSet<KeyValuePair<string,object>> ();

		worldData.Add(new KeyValuePair<string, object>("hasOre", (inventory.numOre > 0) ));
		worldData.Add(new KeyValuePair<string, object>("hasLogs", (inventory.numLogs > 0) ));
		worldData.Add(new KeyValuePair<string, object>("hasFirewood", (inventory.numFirewood > 0) ));
		worldData.Add(new KeyValuePair<string, object>("hasTool", (inventory.tool != null) ));
		worldData.Add(new KeyValuePair<string, object>("isNight", (inventory.localtime.timeofday == TimeTracker.TimeOfDay.NIGHT)));
		worldData.Add(new KeyValuePair<string, object>("isHungry", (inventory.energy <= 0) ));
		worldData.Add(new KeyValuePair<string, object>("isThirsty", (inventory.hydration <= 0)));
		worldData.Add(new KeyValuePair<string, object>("hasRawFood", (inventory.numRawFood > 0)));
		worldData.Add(new KeyValuePair<string, object>("hasFood", (inventory.numFood > 0)));


		return worldData;
	}

	/**
	 * Implement in subclasses
	 */
	public abstract HashSet<KeyValuePair<string,object>> createGoalState ();


	public void planFailed (HashSet<KeyValuePair<string, object>> failedGoal)
	{
		// Not handling this here since we are making sure our goals will always succeed.
		// But normally you want to make sure the world state has changed before running
		// the same goal again, or else it will just fail.
	}

	public void planFound (HashSet<KeyValuePair<string, object>> goal, Queue<GoapAction> actions)
	{
		// Yay we found a plan for our goal
		Debug.Log ("<color=green>Plan found</color> "+GoapAgent.prettyPrint(actions));
	}

	public void actionsFinished ()
	{
		// Everything is done, we completed our actions for this gool. Hooray!
		Debug.Log ("<color=blue>Actions completed</color>");
	}

	public void planAborted (GoapAction aborter)
	{
		// An action bailed out of the plan. State has been reset to plan again.
		// Take note of what happened and make sure if you run the same goal again
		// that it can succeed.
		Debug.Log ("<color=red>Plan Aborted</color> "+GoapAgent.prettyPrint(aborter));
	}

	public bool moveAgent(GoapAction nextAction) {
		// move towards the NextAction's target
		// original movement:
		//float step = moveSpeed * Time.deltaTime;
		//gameObject.transform.position = Vector3.MoveTowards(gameObject.transform.position, nextAction.target.transform.position, step);

		// change navmesh values based on mood
		if (startingMovement == false)
		{
			navmesh.speed = inventory.MoodModifier(navspeed);
			navmesh.acceleration = inventory.MoodModifier(acceleration);
			navmesh.stoppingDistance = inventory.MoodModifier(stoppingDistance);
			
			startingMovement = true;
			// make movement
			navmesh.destination = nextAction.target.transform.position;
		}

		// match animation to local velocity
		Vector3 velocity = navmesh.velocity; // get velocity
		Vector3 localvelocity = transform.InverseTransformDirection(velocity); // transform global navmesh data to local
		float speed = localvelocity.z; // get forward movement speed
		animator.SetFloat("forwardspeed", speed); // set blend tree animator of child to speed

		// measure distance to target
		float distance = Vector3.Distance(transform.position, nextAction.target.transform.position); 

		if (distance < distanceToReach )  // close enough
		{
			// reached target location
			startingMovement = false;
			nextAction.setInRange(true);
			animator.SetFloat("forwardspeed", 0); // set speed back to zero
			return true;
		} 
		else
		{
			return false;
		}
			
	}
}

