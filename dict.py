# (C) 2019-2020 lifegpc
# This file is part of bili.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
def delli(l:list,i) -> (list,int):
    r=[]
    a=-1
    b=0
    for j in l:
        if i!=j :
            r.append(j)
        else :
            a=b
        b=b+1
    return r,a
def dellk(l:list,i:int) -> list:
    r=[]
    a=0
    for k in l:
        if a!=i :
            r.append(k)
        a=a+1
    return r
