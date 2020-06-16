# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:38:21 2020

@author: joaom
"""

import matplotlib.pyplot as plt

Map=[[(0,0),(0,0.3),(0.2,0.3),(0.2,0.7),(0,0.7),(0,1),(0.3,1),(0.3,0.8),(0.7,0.8),(0.7,1),(1,1),(1,0.7),(0.8,0.7),(0.8,0.3),(1,0.3),(1,0),(0.7,0),(0.7,0.2),(0.3,0.2),(0.3,0)],[(0.5,0.3),(0.5,0.6),(0.6,0.4),(0.59,0.29)]]
Slope=[]
Shift=[]

def plot_map():
    # Plots map
    Set=[]
    series=[[],[]]
    for area in Map:
        for point in area:
            series[0].append(point[0])
            series[1].append(point[1])
        Set.append(series)

def split_square(square):
    # Splits square area into 4 equal square areas
    width=square[1]/2
    height=square[2]/2
    obstacle=square[3]
    if obstacle!=1 and obstacle!=0:
        square1=[square[0],width,height,is_object(square[0],width,height)]
        square2=[(square[0][0],square[0][1]+width),width,height,is_object((square[0][0],square[0][1]+width),width,height)]
        square3=[(square[0][0]+height,square[0][1]),width,height,is_object((square[0][0]+height,square[0][1]),width,height)]
        square4=[(square[0][0]+height,square[0][1]+width),width,height,is_object((square[0][0]+height,square[0][1]+width),width,height)]
    else:
        square1=[square[0],width,height,obstacle]
        square2=[(square[0][0],square[0][1]+width),width,height,obstacle]
        square3=[(square[0][0]+height,square[0][1]),width,height,obstacle]
        square4=[(square[0][0]+height,square[0][1]+width),width,height,obstacle]
    return [square1,square2, square3, square4]


void precalc_values() {

  int   i, j=polyCorners-1 ;

  for(i=0; i<polyCorners; i++) {
    if(polyY[j]==polyY[i]) {
      constant[i]=polyX[i];
      multiple[i]=0; }
    else {
      constant[i]=polyX[i]-(polyY[i]*polyX[j])/(polyY[j]-polyY[i])+(polyY[i]*polyX[i])/(polyY[j]-polyY[i]);
      multiple[i]=(polyX[j]-polyX[i])/(polyY[j]-polyY[i]); }
    j=i; }}

bool pointInPolygon() {

  int   i, j=polyCorners-1 ;
  bool  oddNodes=NO      ;

  for (i=0; i<polyCorners; i++) {
    if ((polyY[i]< y && polyY[j]>=y
    ||   polyY[j]< y && polyY[i]>=y)) {
      oddNodes^=(y*multiple[i]+constant[i]<x); }
    j=i; }

  return oddNodes; }        
    
def precalc():
    
    for area in Map:


def point_in_polygon(point):
    # Check if point is inside polygon
    score=0
    for area in Map:
        for i in range(len(area)):
            a=area[i-1]
            b=area[i]
            if (a[0]<point[0] || a[1]<point[1]):
                
            
    
def is_object(point, width, height):
    # Checks probability of area containing an obstacle
    corners=[point, [point[0],point[1]+height], [point[0]+width,point[1]], [point[0]+width,point[1]+height]]
    score=0
    for point in corners:
        score+=(point_in_polygon(point)*0.25)
    return score
    
        
for i in range(11):
    