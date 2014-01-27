import wolframalpha as wa
appId2 = 'Q59EW4-7K8AHE858R' #working
appId = 'HY3K3J-K9L6QTWQ8G'
appId3 = 'HY3K3J-EQQTHQJK87'
client = wa.Client(appId)
res = client.query('2 multiply 10')
results = list(res.results)
print(results[0].text)