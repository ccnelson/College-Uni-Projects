// C NELSON UoH 2020

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RotateAroundCentre : MonoBehaviour
{
    void Update()
    {
        //transform.RotateAround(Vector3.forward, Vector3.up, 100 * Time.deltaTime);

        transform.Rotate(Time.deltaTime * 100, 0, 0);
    }
}
