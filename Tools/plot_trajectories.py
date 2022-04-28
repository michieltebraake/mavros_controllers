import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt

folder = '/home/michiel/uav_mpcc/recordings/'

bags_list = {
    '-': ['normal'],
    # '8.5485': ['normal1', 'motor_constant_8_648', 'motor_constant_8_558'],
    # '1e-6': ['normal1', 'rolling_moment_0', 'rolling_moment_2', 'rolling_moment_4', 'rolling_moment_10', 'rolling_moment_100'],
    '0.000806428': ['rotor_drag_008']
}

for (baseline, bags) in bags_list.items():
    data_columns = ['pose.position.x', 'pose.position.y', 'pose.position.z',
                    'twist.angular.x', 'twist.angular.y', 'twist.angular.z']
    # column_names = ['x', 'y', 'z']

    # '/record_data/local_position/velocity_body': ['twist.angular.x', 'twist.angular.y', 'twist.angular.z'],

    topics = {'mavros/local_position/pose': ['pose.position.x', 'pose.position.z']}

    loaded_bags = { bag_name : bagreader(folder + bag_name + '.bag') for bag_name in bags }

    ax = None
    for (bag_name, bag) in loaded_bags.items():
        pose_msg = bag.message_by_topic('mavros/local_position/pose')
        df = pd.read_csv(pose_msg)

        if ax is None:
            ax = df.plot(x='pose.position.x', y='pose.position.y', label=bag_name, title=f'Baseline: {baseline}')
        else:
            df.plot(x='pose.position.x', y='pose.position.y', label=bag_name, ax=ax)

    # for (topic, show_columns) in topics.items():

    #     for show_column in show_columns:
    #         ax = None



    # for (bag_name, bag) in loaded_bags.items():
    #     pose_msg = bag.message_by_topic(topic)
    #     df = pd.read_csv(pose_msg)

    #     filtered = [col for col in df.columns if col in show_column]
    #     renamed = filtered

    #     for column in show_columns:
    #         renamed = [col.replace(column, bag_name) for col in renamed]

    #     renamed_columns = dict(zip(filtered, renamed))
    #     df = df.rename(renamed_columns, axis=1)

    #     if ax is not None:
    #         df[renamed].plot(ax=ax)
    #     else:
    #         ax = df[renamed].plot(title=str(show_column))


plt.show()