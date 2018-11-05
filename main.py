import docker


docker_file_path = '/home/ubuntu/vaibhav'
tag_name = 'vaibhavkholase/vaibhavtest'
container_name= 'mypytest'
client = docker.from_env()

print("Start Building your docker image...")
##### Building an Image form given DockerFile##########
client.images.build(path=docker_file_path,tag=tag_name)

image = client.images.get(tag_name)
print(image.short_id)

print("pushing image...")

aauth_config ={
              'username':'vaibhavkholase',
              'password':'devops123'
             }

###using authentication pushing docker image
client.images.push('vaibhavkholase/vaibhavtest', tag='latest', auth_config=aauth_config)
print("pushing of an image is done.")
# Check if image is already present at local server
if "docker image inspect vaibhavkholase/vaibhavtest >/dev/null 2>&1  && echo yes || echo NO = 'yes'":
    print("Docker image is already exist")

else: 
      print("pulling imgae to local machine")
      client.images.pull('vaibhavkholase/vaibhavtest')


print("Now running new container from the local image")
client.containers.run('vaibhavkholase/vaibhavtest',detach=True,ports={'80/tcp' : 80})
print("'Congrtas', you have successfully deployed your python web application")

