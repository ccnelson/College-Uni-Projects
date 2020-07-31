// C NELSON UoH 2020
// Component class for interactable objects

using UnityEngine;
using TMPro;

// Tracks agent resources
public class InventoryComponent : MonoBehaviour
{
    // attributes all set to private with getters and setters. 
    // changing a value notifies a handler which is prompted to 
    // change text displayed. A lot of code, but saves updating text
    // thousands of time when no change has taken place.

    // tool
    private GameObject m_tool;
    public GameObject tool
    {
        get { return m_tool; }
        set 
        {
            if (m_tool == value) return;
            m_tool = value;
            OnVariableChange?.Invoke();
        }
    }

    // logs
    private int m_numLogs = 0;
    public int numLogs
    {
        get { return m_numLogs; }
        set
        {
            if (m_numLogs == value) return;
            m_numLogs = value;
            OnVariableChange?.Invoke();
        }
    }

    // firewood
    private int m_numFirewood = 0;
    public int numFirewood
    {
        get { return m_numFirewood; }
        set
        {
            if (m_numFirewood == value) return;
            m_numFirewood = value;
            OnVariableChange?.Invoke();
        }
    }

    // ore
    private int m_numOre = 0;
    public int numOre
    {
        get { return m_numOre; }
        set
        {
            if (m_numOre == value) return;
            m_numOre = value;
            OnVariableChange?.Invoke();
        }
    }

    // rawfood
    private int m_numRawFood = 0;
    public int numRawFood
    {
        get { return m_numRawFood; }
        set
        {
            if (m_numRawFood == value) return;
            m_numRawFood = value;
            OnVariableChange?.Invoke();
        }
    }

    // food
    private int m_numFood = 0;
    public int numFood
    {
        get { return m_numFood; }
        set
        {
            if (m_numFood == value) return;
            m_numFood = value;
            OnVariableChange?.Invoke();
        }
    }

    // hydration
    private int m_hydration = 5;
    public int hydration
    {
        get { return m_hydration; }
        set
        {
            if (m_hydration == value) return;
            m_hydration = value;
            OnVariableChange?.Invoke();
        }
    }

    // energy
    private int m_energy = 5;
    public int energy
    {
        get { return m_energy; }
        set
        {
            if (m_energy == value) return;
            m_energy = value;
            OnVariableChange?.Invoke();
        }
    }

    // extroversion (mood)
    public enum Extroversion
    {
        FEEL = 1,
        INTUIT = 2,
        SENSE = 3,
        THINK = 4
    }
    private Extroversion m_extroversion = Extroversion.FEEL;
    public Extroversion extroversion
    {
        get { return m_extroversion; }
        set
        {
            if (m_extroversion == value) return;
            m_extroversion = value;
            OnVariableChange?.Invoke();
        }
    }

    private System.Random random_no = new System.Random();
    public TimeTracker localtime;
	public GameObject toolPrefab = null;
	public Transform handTransform = null;
    public TextMeshPro text;


    // delegate event pair for tracking property changes
    public delegate void OnVariableChangeDelegate();
    public event OnVariableChangeDelegate OnVariableChange;


    private void Start()
	{
		localtime = FindObjectOfType(typeof(TimeTracker)) as TimeTracker;
        text = GetComponentInChildren<TextMeshPro>(); // get text

        // initialise handlers
        OnVariableChange += VariableChangeHandler;

        text = GetComponentInChildren<TextMeshPro>();
        text.text = "Ext: \t" + extroversion +
                    "\nTool: \t" + tool +
                    "\nHydr: \t\t" + hydration +
                    "\nEnergy: \t" + energy +
                    "\nLogs: \t\t" + numLogs +
                    "\nFirewood: \t" + numFirewood +
                    "\nOre: \t\t" + numOre +
                    "\nFood: \t" + numFood +
                    "\nRawFood: \t" + numRawFood;
    }

    // mood change method
    public void DetermineMood()
    {
        int rand = random_no.Next(1, 5);
        extroversion = (Extroversion)rand;
    }

    // event handler
    private void VariableChangeHandler()
    {
        text.text = "Ext: \t" + extroversion +
                    "\nTool: \t" + tool +
                    "\nHydr: \t\t" + hydration +
                    "\nEnergy: \t" + energy +
                    "\nLogs: \t\t" + numLogs +
                    "\nFirewood: \t" + numFirewood +
                    "\nOre: \t\t" + numOre +
                    "\nFood: \t" + numFood +
                    "\nRawFood: \t" + numRawFood;
    }
    

    // overloaded mood modifiers
    public int MoodModifier(int number)
    {
        return (number * (int)extroversion);
    }

    public float MoodModifier(float number)
    {
        return (number * (float)(int)extroversion);
    }
}

