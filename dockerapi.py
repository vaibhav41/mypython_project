import docker

##image_name='pytest'
####Declaring variables for create image & container

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
##	      'registry':'https://index.docker.io/v1/'	
             }

#client.login(username='vaibhavkholase', password='devops123')
###using authentication pushing docker image
client.images.push('vaibhavkholase/vaibhavtest', tag='latest', auth_config=aauth_config)
print("pushing of an image is done.")

# Now pulling above image locally
print("pulling Image locally")
client.images.pull('vaibhavkholase/vaibhavtest')
client.images.list()
print("Now running new container from the local image")
client.containers.run('vaibhavkholase/vaibhavtest',detach=True,ports={'80/tcp' : 80})
print("'Congrtas', you have successfully deployed your python web application")

