from java.util import ArrayList

def create(id, type, values):
   return factory.configurationItem(id, type, values)

def verifyNoValidationErrors(entity):
   print "Validaing ci of type:", entity.type
   if entity.validations is None or len(entity.validations) == 0:
       return entity
   else:
       raise Exception("Validation errors are present! " + entity.validations.toString())

def verifyNoValidationErrorsInRepoObjectsEntity(repositoryObjects):
   for repoObject in repositoryObjects:
       verifyNoValidationErrors(repoObject)

def saveRepositoryObjectsEntity(repoObjects):
    print "Saving repository objects"
    objectsToSave = [i for i in repoObjects if not repository.exists(i.id) ]
    repositoryObjects = repository.create(objectsToSave)
    verifyNoValidationErrorsInRepoObjectsEntity(repositoryObjects)
    print "Saved repository objects"
    return repositoryObjects

def save(listOfCis):
	return saveRepositoryObjectsEntity(listOfCis)




infrastructureList = []

infrastructureList.append(create('Infrastructure/localhost','overthere.LocalHost',{'tags':[],'os':'UNIX','deploymentGroup':'0'}))
infrastructureList.append(create('Infrastructure/localhost/demo','demo.Server',{'tags':[],'home':'/tmp','host':'Infrastructure/localhost','envVars':{},'deploymentGroup':'0'}))
infrastructureList.append(create('Infrastructure/localhost/demo/folder','demo.Folder',{'tags':[],'directory':'/tmp/folder','envVars':{},'permissions':'777','server':'Infrastructure/localhost/demo','deploymentGroup':'0'}))
infrastructureList.append(create('Infrastructure/localhost/demo/folder/petclinic','demo.WarModule',{'container':'Infrastructure/localhost/demo/folder','deployable':'Applications/PetClinic-war/1.0-13/petclinic','placeholders':{}}))
save(infrastructureList)


environmentsList = []

environmentsList.append(create('Environments/TEST','udm.Environment',{'dictionaries':[],'triggers':[],'members':['Infrastructure/localhost','Infrastructure/localhost/demo/folder','Infrastructure/localhost/demo']}))
save(environmentsList)


configurationList = []

save(configurationList)
