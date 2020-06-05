// CHRIS NELSON NHC 2018
// this abstract class provides movement
// as speed, direction, and rotation
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class Character : MonoBehaviour 
{
	[SerializeField] // we can monitor and change in editor
	public float speed;
	protected Vector3 direction;
	protected Vector3 rot;
	
	protected virtual void Update () // virtual can be overridden by subclass
	{
		Move();
	}

	public void Move()
	{
		transform.Translate (direction * speed * Time.deltaTime);
		transform.Rotate (rot * Time.deltaTime);
	}
}
