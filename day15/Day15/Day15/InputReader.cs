using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Day15.Interface;
using System.Configuration;
using System.Diagnostics;
using System.Text.RegularExpressions;
using Day15.Model;

namespace Day15
{
    class InputReader : IInputReader
    {
        

        private string filepath = ConfigurationManager.AppSettings["filepath"];
        private Solution _solution;

        public InputReader(Solution solution)
        {
            _solution = solution;
        }
        public void Parse()
        {
            foreach(var line in System.IO.File.ReadAllLines(filepath))
            {
                int type = 0;
                foreach(var lines in line.Split(new string[] { "closest" }, StringSplitOptions.None))
                {
                    GrabCoordinates(lines, type);
                    type = 1 - type;
                }
            }
        }
        private void GrabCoordinates(string line, int type)
        {
            Regex rx = new Regex(@"-?\d+");
            var matches = rx.Matches(line);
            int x = int.Parse(matches[0].Groups[0].Value);
            int y = int.Parse(matches[1].Groups[0].Value);
            if (type == 0)
            {
                _solution.Sensors.Add(new Sensor(x, y));
            }
            else
            {
                _solution.Beacons.Add(new Beacon(x, y));
            }
            _solution.Set.Add((x, y));
        }
    }
}
