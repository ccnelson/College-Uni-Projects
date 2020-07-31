// C NELSON UoH 2020

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class TimeTracker : MonoBehaviour
{
    private TreeComponent[] trees = null;
    private IronRockComponent[] rocks = null;
    private FarmComponent[] farms = null;

    public bool timeToReplenish = false;
    private int replenish = 2;
    
    public enum TimeOfDay
    {
        MORNING,
        AFTERNOON,
        EVENING,
        NIGHT
    }
    public TimeOfDay timeofday;

    private IEnumerator coroutine;


    private void Start()
    {
        // sun replenishes natural stocks
        trees = FindObjectsOfType(typeof(TreeComponent)) as TreeComponent[];
        rocks = FindObjectsOfType(typeof(IronRockComponent)) as IronRockComponent[];
        farms = FindObjectsOfType(typeof(FarmComponent)) as FarmComponent[];
    }

    void LateUpdate()
    {
        // check position of sun
        if (transform.position.y > 90) 
        {
            timeofday = TimeOfDay.AFTERNOON;
        }
        else if (transform.position.y < -90)
        {
            timeofday = TimeOfDay.NIGHT;
        }
        else if (transform.position.z < -90)
        {
            timeofday = TimeOfDay.MORNING;
        }
        else if (transform.position.z > 90)
        {
            timeofday = TimeOfDay.EVENING;
            timeToReplenish = true;
        }

        if (timeToReplenish == true && timeofday == TimeOfDay.NIGHT)
        {
            // use a coroutine to let actions take
            // several frames
            coroutine = replenishAll();
            StartCoroutine(coroutine);
            timeToReplenish = false;
        }    
    }

    private void Update()
    {
        // allows switching between test scenes
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            SceneManager.LoadScene("test_area");
        }
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            SceneManager.LoadScene("test_town");
        }
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Application.Quit();
        }


    }


    private IEnumerator replenishAll()
    {
        foreach (TreeComponent tree in trees)
        {
            tree.treeResource = replenish;
            yield return new WaitForSeconds(0.0f);
        }
        foreach (IronRockComponent rock in rocks)
        {
            rock.rockResource = replenish;
            yield return new WaitForSeconds(0.0f);
        }
        foreach (FarmComponent farm in farms)
        {
            farm.farmResource = replenish;
            yield return new WaitForSeconds(0.0f);
        }
    }
}
