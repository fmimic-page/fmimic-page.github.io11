import os
import subprocess

def compress_all_videos(folder_path, target_bitrate, new_resolution):
    for filename in os.listdir(folder_path):
        if filename.endswith('Pizza.mp4'):
            input_path = os.path.join(folder_path, filename)
            temp_output_path = os.path.join(folder_path, "temp_" + filename)
            print(f"Compressing {filename} to {new_resolution}...")

            # 构建 FFmpeg 命令
            command = [
                'ffmpeg',
                '-i', input_path,
                '-vf', f'scale={new_resolution[0]}:{new_resolution[1]}',
                '-b:v', target_bitrate,
                temp_output_path
            ]

            # 运行 FFmpeg 命令
            subprocess.run(command)

            # 用临时文件覆盖原始文件
            os.replace(temp_output_path, input_path)

            print(f"Finished compressing {filename}")

# 使用示例
compress_all_videos('/home/cuite/VLMimic.github.io/static/videos', '500k', (720, 480))
