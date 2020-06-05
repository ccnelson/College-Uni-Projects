// CHRIS NELSON NHC 2018
// cycles through instances
// tagged as globs, randomising
// animation speed each time
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GlobScript : MonoBehaviour 
{
	public GameObject[] all_globs; // holds a list of active globs
	public Animator anim; // will hold each globs animator, once, when looping below

	void Start () 
	{
		// populate list
		all_globs = GameObject.FindGameObjectsWithTag("globs");
		// iterate list, updating animator, and its speed each iteration
		foreach (GameObject glob in all_globs)
		{
			anim = glob.GetComponent<Animator>();
			anim.speed = Random.Range(0.1f, 1.9f);
		}
	}
}
