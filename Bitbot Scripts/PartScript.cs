// CHRIS NELSON NHC 2018
// randomises parts animation frame.
// animation is paused, but frames
// provide different part designs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PartScript : MonoBehaviour 
{
	Animator anim;
	void Start () 
	{
		anim = GetComponent<Animator> ();
		anim.Play("parts", 0, Random.Range(0f, 1f));
	}
}
