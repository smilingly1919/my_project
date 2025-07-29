import numpy as np
import sdf_helper as sh

def load_density(file_path, species):
    """
    加载指定粒子种类的坐标和场数据。

    参数:
    - file_path: str, SDF 文件路径
    - species: str, 粒子种类，如 'Photon'、'Electron'

    返回:
    - dict 包含 'x','y','z' 坐标和归一化密度 'ne'，平均能量 'ek'
    """
    data = sh.getdata(file_path)

    # 坐标轴数据，单位同SDF文件，通常是米
    grid_data = data.Grid_Grid_mid.data
    x = np.array(grid_data[0])
    y = np.array(grid_data[1])
    z = np.array(grid_data[2]) if len(grid_data) == 3 else None

    # 读取粒子相关数据
    ne = getattr(data, f"Derived_Number_Density_{species}").data
    ek = getattr(data, f"Derived_Average_Particle_Energy_{species}").data

    return {'x': x, 'y': y, 'z': z, 'ne': ne, 'ek': ek}


def load_field(file_path):
    """
    加载电场和磁场数据。

    参数:
    - file_path: str, SDF 文件路径

    返回:
    - dict 包含电场分量 'Ex','Ey','Ez' 和磁场分量 'Bx','By','Bz'
    """
    data = sh.getdata(file_path)
    grid_data = data.Grid_Grid_mid.data
    x = np.array(grid_data[0])
    y = np.array(grid_data[1])
    z = np.array(grid_data[2]) if len(grid_data) == 3 else None
    return {
        'Ex': data.Electric_Field_Ex.data,
        'Ey': data.Electric_Field_Ey.data,
        'Ez': data.Electric_Field_Ez.data,
        'Bx': data.Magnetic_Field_Bx.data,
        'By': data.Magnetic_Field_By.data,
        'Bz': data.Magnetic_Field_Bz.data,
        'x': x, 'y': y, 'z': z,
    }


def load_idall(file_path, species, subset):
    """
    加载指定粒子子集的空间位置和动量数据。

    参数:
    - file_path: str, SDF 文件路径
    - species: str, 粒子类型，如 'Photon'、'Electron'
    - subset: str, 子集名称，如 'testp', 'teste'

    返回:
    - dict 包含位置坐标 'x','y','z' 和动量分量 'px','py','pz'
    """
    data = sh.getdata(file_path)

    # 位置
    pos_key = f"Grid_Particles_{subset}_{species}"
    grid = getattr(data, pos_key).data
    x, y, z = np.array(grid[0]), np.array(grid[1]), np.array(grid[2])

    # 动量
    px = getattr(data, f"Particles_Px_{subset}_{species}").data
    py = getattr(data, f"Particles_Py_{subset}_{species}").data
    pz = getattr(data, f"Particles_Pz_{subset}_{species}").data

    return {'x': x, 'y': y, 'z': z, 'px': px, 'py': py, 'pz': pz}

def load_distfun(file_path, species, dist_type):
    data = sh.getdata(file_path)

    dist_key = f"dist_fn_{dist_type}_{species}"
    grid_key = f"Grid_{dist_type}_{species}"

    dist = getattr(data, dist_key).data
    grid = getattr(data, grid_key).data

    if isinstance(grid, tuple):
        return {
            'dist': dist,
            'grid_x': grid[0],
            'grid_y': grid[1],
        }
    else:
        return {
            'dist': dist,
            'grid': grid,
        }




