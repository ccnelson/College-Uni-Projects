// CHRIS NELSON NHC 2018
// randomises crates animation frame.
// animation is paused, but frames
// provide different crate designs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CrateOScript : MonoBehaviour 
{
	Animator anim;
	void Start () 
	{
		anim = GetComponent<Animator> ();
		anim.Play("crate_options", 0, Random.Range(0f, 1f));
	}
}
