// CHRIS NELSON NHC 2018
// makes camera follow player
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour 
{
	public GameObject player;
	private Vector3 offset;

	void Start () 
	{
		offset = transform.position - player.transform.position;
	}
	
	void LateUpdate () // runs after everything else
	{ 
		transform.position = player.transform.position + offset;
	}
}
