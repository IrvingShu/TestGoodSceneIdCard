import os
import sys
import json

if __name__ == "__main__":
    with open('./idProbe_features_list.json') as f, open('./good_scene_index.txt') as f1, open('./good_scene.json', 'w') as f2:
        load_dict = json.load(f)
        print(str(len(load_dict['path'])))
        print(str(len(load_dict['id'])))
        scene = []
        scene_label = []

        lines = f1.readlines()
        print('read good scene: %d' %len(lines))
        for line in lines:
            img_index = line.strip()
            i = 0
            k = 0        
            for path in load_dict['path']:
                
                json_img_index = path.split('/')[-1].split('.')[0]
                img_type = path.split('/')[0]
                
                if img_index == json_img_index and img_type == 'scene':
                    if k > 0:
                        print(path)
                    k = k + 1
                    json_img_label = load_dict['id'][i]
                    scene.append(path)
                    scene_label.append(json_img_label)
                    
                    for j in range(len(load_dict['id'])):
                        if json_img_label == load_dict['id'][j] and i!= j:
                            scene.append(load_dict['path'][j])
                            scene_label.append(json_img_label)
                    
                i = i + 1
        save_dict = {}
        save_dict['path'] = scene
        save_dict['id'] = scene_label
        json.dump(save_dict, f2)
        print('all: %d'%len(scene))        
            
