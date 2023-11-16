#!/usr/bin/env python3
import vtk
import sys

if len(sys.argv)>=3:
    filename=sys.argv[1]
    output=sys.argv[2]

    reader=vtk.vtkDataSetReader()
    reader.SetFileName(filename)
    reader.Update()

    f=open(output,"w")
    for i in range(reader.GetOutput().GetNumberOfPoints()):
        p=reader.GetOutput().GetPoint(i)
        r=reader.GetOutput().GetPointData().GetArray("RADIUS").GetTuple1(i)
        f.write("{} {} {} {}\n".format(p[0],p[1],p[2],r))

    f.close()