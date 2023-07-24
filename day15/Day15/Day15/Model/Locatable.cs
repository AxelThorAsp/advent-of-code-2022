using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day15.Model
{
    abstract class Locatable
    {
        public int X { get; private set; }
        public int Y { get; private set; }

        public Locatable() { }
        public Locatable(int x, int y)
        {
            X = x;
            Y = y;
        }
        public int ManhattanDistance(Locatable point)
        {
            return Math.Abs(X - point.X) + Math.Abs(Y - point.Y);
        }
        public int ManhattanDistance((int X, int Y) point)
        {
            return Math.Abs(X - point.X) + Math.Abs(Y - point.Y);
        }
        public override bool Equals(Object obj)
        {
            if (!(obj is Locatable)) return false;

            Locatable p = (Locatable)obj;
            return X == p.X & Y == p.Y;
        }

        public override int GetHashCode()
        {
            return X ^ Y;
        }
    }
}
