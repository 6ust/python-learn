import numpy as np

def build_tree(data, label, tree, depth=1):
	classes, counts = np.unique(labels, return_counts=True)
	n_classes = classes.shapes[0]

	# Criterio de parada
	if not stopping_criterion(n_classes, depth, tree.max_depth):
		node = Node()

		# encontra o melhor ponto de corte dado a regiao atual do espaço
		# de acordo com o criterio de impureza escolhido
		feature, threshold = find_cut_point(data, labels, tree.impurity_criterion)

		# aplicando o limiar para particionar o espaço
		mask = data[:, feature] <= threshold

		# construindo arvore recursivamente para 
		# os sub-espaço da direita para a esquerda
		left = build_tree(data[mask], label[mask], tree, depth + 1)
		right = build_tree(data[~mask], label[~mask], tree, depth + 1)


		return Node(feature=feature, threshold=threshold, left=left, right=right)

		# calcula a quantidade de exemplos por classe nesse no folha
		# e instancia um no folha com essas  quantidades, lembre-se que isso
		# sera usado na predição

		values = np.zeros(tree.n_classes)
		values[classes] = counts
		return Node(is_leaf=True, counts=values)



def entropy_criterion(data, labels):
	""" Entropy
	Parameters
	----------
	data: numpy array-like = [n_samples, n_features]
	labels: numpy array-like, shape = [n_samples]

	Return
	------
	entropy: float
	"""
	classes = np.unique(labels)

	s = 0
	for c in classes:
		p = np.mean(labels == c)
		s -= p * np.log(p)

	return s
  

def gini_criterion(data, labels):
	""" Gini Index
	Parameters
	----------
	data: numpy array-like = [n_samples, n_features]
	labels: numpy array-like, shape = [n_samples]

	Return
	------
	gini: float
	"""
	classes = np.unique(labels)

	s = 0
	for c in classes:
		p = np.mean(labels == c)
		s += p * (1 - p)
    
	return s

def entropy_criterion(data, labels):
	""" Entropy
	Parameters
	----------
	data: numpy array-like = [n_samples, n_features]
	labels: numpy array-like, shape = [n_samples]

	Return
	------
	entropy: float
	"""
	classes = np.unique(labels)

	s = 0
	for c in classes:
		p = np.mean(labels == c)
		s -= p * np.log(p)
    
	return s
  

def gini_criterion(data, labels):
	""" Gini Index
	Parameters
	----------
	data: numpy array-like = [n_samples, n_features]
	labels: numpy array-like, shape = [n_samples]

	Return
	------
	gini: float
	"""
	classes = np.unique(labels)

	s = 0
	for c in classes:
		p = np.mean(labels == c)
		s += p * (1 - p)
	    
	return s

def find_cut_point(data, labels, impurity_criterion = gini_criterion):
	"""find the best point 

	Parameters
	----------
	data: numpy array-like = [n_samples, n_features]
	labels: numpy array-like, shape = [n_samples]
	impurity: callable, default=gini_criterion

	Return
	-------
	feature,  threshold
	"""

	n_samples, n_features = data.shape

	max_info_gain = np.iinfo(np.int32).min
	feat_id = 0
	best_threshold = 0

	# pre-calculando a impureza da regiao atual
	H_parent = impurity_criterion(data, labels)

	# para cada um dos atributos
	# vamos tentar encontrar o limiar que maximiza o ganho de informação
	for j in range(n_features):
		# so interessa os valores ordenados unicos
		# do atributo j nessa regiao espaço

		values = np.unique(data[:, j])

		for i in range(values.shape[0] - 1):
			# usamos o ponto medio dos valores possiveis
			# como limiar candidato para o ponto de corte

			threshold = (values[i] + values[i + 1]) / 2

			mask = data[:, j] <= threshold

			info_gain = H_parent \
			 		  - (mask.sum() * impurity_criterion(data[mask],labels[mask])) \
			 		  + (~mask.sum() * impurity_criterion(data[~mask],labels[~mask])) \
					  / float(n_samples)

			if max_info_gain < info_gain:
				best_threshold = threshold
				feat_id = j
				max_info_gain = info_gain

		return feat_id, best_threshold