using System;
using System.Collections.Generic;
using System.Diagnostics;
using Day15.Interface;
using Day15.Model;


namespace Day15
{
    class Solution : ISolution
    {
        public List<Locatable> Beacons = new List<Locatable>();
        public List<Locatable> Sensors = new List<Locatable>();
        public HashSet<(int, int)> Set = new HashSet<(int,int)>();
        private int jump;
        public void Run()
        {
            new InputReader(this).Parse();
            Solve();
        }
        private void Solve()
        {
            int limit = 4000000;
            int x = 0;
            int y = 0;
            outer:
            while (x <= limit)
            {
                Debug.WriteLine(x);
                jump = 0;
                while (y <= limit)
                {
                    if (Set.Contains((x, y)) || (InRange((x, y)))) 
                    {
                        y += jump;
                    }
                    else
                    {
                        Debug.WriteLine(x * limit + y);
                        return;
                    }
                }
                x++;
            }
        }
        private bool InRange((int, int) point)
        {
            for (int i = 0; i < Sensors.Count; i++)
            {
                if (Sensors[i].ManhattanDistance(point) <= Sensors[i].ManhattanDistance(Beacons[i])) {
                    jump = Sensors[i].ManhattanDistance(Beacons[i]);
                    return true; 
                }
            }
            return false;
        }
    }
}
