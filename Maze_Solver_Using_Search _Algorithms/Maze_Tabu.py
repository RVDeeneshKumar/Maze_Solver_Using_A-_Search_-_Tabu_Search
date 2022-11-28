from pyamaze import *

def Tabu(m, start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    Tabu_Path={}
    TSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        TSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                Tabu_Path[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[Tabu_Path[cell]]=cell
        cell=Tabu_Path[cell]
    return TSeacrh,Tabu_Path,fwdPath

def main2(n, speed):


    m_1=maze(n,n)
    m_1.CreateMaze(loadMaze='maze--2022-05-23--17-57-41.csv')

    TSeacrh,TabuPath,fwdPath = Tabu(m_1)

    a_1=agent(m_1,n,n,footprints=True,shape='square',color=COLOR.green,filled=True)
    b_1=agent(m_1,1,1,footprints=True,filled=True,color=COLOR.cyan)
    c_1=agent(m_1,n,n,footprints=True,color=COLOR.yellow,filled=True)
    m_1.tracePath({a_1:TSeacrh},showMarked=True, delay=speed)
    m_1.tracePath({b_1:TabuPath},delay=speed)
    m_1.tracePath({c_1:fwdPath},delay=speed)

    l_1 = textLabel(m_1, 'Tabu Path Length', len(fwdPath) + 1)
    l_1 = textLabel(m_1, 'Tabu Search Length', len(TabuPath))

    m_1.run()
