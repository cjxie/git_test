## Image

	pull
	push
	rmi
	search

	docker commit -m="" -a="" containerId imageName
	docker buildx build (absoluet path of Dockfile)
	docer tag Image Image:Tag
		
## Docker容器互联
	
	docker run -d -p/-P imageName Command
	-p 127.0.0.1:5001:5000 assign container port to designated host port
	-P random port on the host
	
	docker network create -d bridge test-net
	docker run -itd --name test1 --network test-net ImageName Command
	
	## test connection
	ping anotherContainerName
	
