// C NELSON UoH 2020
// Abstract action class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)


using UnityEngine;
using System.Collections.Generic;
using UnityEngine.AI;

public abstract class GoapAction : MonoBehaviour {

	protected InventoryComponent inventory;
	protected Animator animator;

	private HashSet<KeyValuePair<string,object>> preconditions;
	private HashSet<KeyValuePair<string,object>> effects;

	private bool inRange = false;
	private Vector3 randomDirection;
	private NavMeshHit hit;

	protected readonly int hydrationConsumed = 1;
	protected readonly int energyConsumed = 1;
	protected readonly float toolDegrade = 0.34f;


	/* The cost of performing the action. 
	 * Figure out a weight that suits the action. 
	 * Changing it will affect what actions are chosen during planning.*/
	public float cost = 1f;

	/**
	 * An action often has to perform on an object. This is that object. Can be null. */
	public GameObject target;


	private void Start()
	{
		inventory = GetComponent<InventoryComponent>();  // find associated inventory
		animator = GetComponentInChildren<Animator>();
	}


	public GoapAction() {
		preconditions = new HashSet<KeyValuePair<string, object>> ();
		effects = new HashSet<KeyValuePair<string, object>> ();
	}

	public void doReset() {
		inRange = false;
		target = null;
		reset ();
	}

	/**
	 * Reset any variables that need to be reset before planning happens again.
	 */
	public abstract void reset();

	/**
	 * Is the action done?
	 */
	public abstract bool isDone();

	/**
	 * Procedurally check if this action can run. Not all actions
	 * will need this, but some might.
	 */
	public abstract bool checkProceduralPrecondition(GameObject agent);

	/**
	 * Run the action.
	 * Returns True if the action performed successfully or false
	 * if something happened and it can no longer perform. In this case
	 * the action queue should clear out and the goal cannot be reached.
	 */
	public abstract bool perform(GameObject agent);

	/**
	 * Does this action need to be within range of a target game object?
	 * If not then the moveTo state will not need to run for this action.
	 */
	public abstract bool requiresInRange ();
	

	/**
	 * Are we in range of the target?
	 * The MoveTo state will set this and it gets reset each time this action is performed.
	 */
	public bool isInRange () {
		return inRange;
	}
	
	public void setInRange(bool inRange) {
		this.inRange = inRange;
	}


	public void addPrecondition(string key, object value) {
		preconditions.Add (new KeyValuePair<string, object>(key, value) );
	}


	public void removePrecondition(string key) {
		KeyValuePair<string, object> remove = default(KeyValuePair<string,object>);
		foreach (KeyValuePair<string, object> kvp in preconditions) {
			if (kvp.Key.Equals (key)) 
				remove = kvp;
		}
		if ( !default(KeyValuePair<string,object>).Equals(remove) )
			preconditions.Remove (remove);
	}


	public void addEffect(string key, object value) {
		effects.Add (new KeyValuePair<string, object>(key, value) );
	}


	public void removeEffect(string key) {
		KeyValuePair<string, object> remove = default(KeyValuePair<string,object>);
		foreach (KeyValuePair<string, object> kvp in effects) {
			if (kvp.Key.Equals (key)) 
				remove = kvp;
		}
		if ( !default(KeyValuePair<string,object>).Equals(remove) )
			effects.Remove (remove);
	}

	
	public HashSet<KeyValuePair<string, object>> Preconditions {
		get {
			return preconditions;
		}
	}

	public HashSet<KeyValuePair<string, object>> Effects {
		get {
			return effects;
		}
	}


	public Vector3 RandomNavmeshPosition(Vector3 origin, float dist, int mask)
	{
		// get a random point in sphere with radius 1, multiply by distance
		randomDirection = UnityEngine.Random.insideUnitSphere * dist;
		// add calling origin
		randomDirection += origin;
		// get nearest valid position on navmesh, store in hit
		// mask relates to mask layer (-1 : all layers)
		NavMesh.SamplePosition(randomDirection, out hit, dist, mask);
		return hit.position;
	}


	public void DegradeTool(ToolComponent tool)
	{
		tool.use(toolDegrade);
		if (tool.destroyed())
		{
			Destroy(inventory.tool);
			inventory.tool = null;
		}
	}
}