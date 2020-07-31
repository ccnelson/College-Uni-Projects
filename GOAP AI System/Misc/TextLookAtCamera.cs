// C NELSON UoH 2020

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextLookAtCamera : MonoBehaviour
{
    private Camera cam;

    void Start()
    {
        cam = Camera.main;
    }


    void Update()
    {
        transform.LookAt(cam.transform);
        transform.rotation = Quaternion.LookRotation(cam.transform.forward);
    }
}
