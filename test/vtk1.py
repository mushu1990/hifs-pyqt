import vtk

# 创建球体
sphere = vtk.vtkSphereSource()
sphere.SetPhiResolution(50)
sphere.SetThetaResolution(50)

# 显示球体
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# 创建渲染器、渲染窗口和交互器
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# 将球体添加到渲染器
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)

render_window.Render()
render_window_interactor.Start()
