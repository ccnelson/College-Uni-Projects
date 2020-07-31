// C NELSON UoH 2020


using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CelestialBodies : MonoBehaviour
{

    public float timescale = 2.5f;
    

    void Update()
    {
        transform.RotateAround(Vector3.zero, Vector3.right, timescale * Time.deltaTime);
        transform.LookAt(Vector3.zero);
    }
}
