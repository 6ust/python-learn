import random

import numpy as np

print("Construcao de Rede Neural")
print()


class Nome(object):
	pass


class Network(object):

	# Size contem o numero de neuronios
	def __init__(self, sizes):

		self.num_layers = len(sizes)
		self.sizes = sizes
		#Biases e weights sao inicializados aleatoriamente com distribuições gaussianas
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]

	def sigmoid_prime(z):
		return 1.0 / (1.0 + np.exp(-z))
	def sigmoid(z):
		return 1.0 / (1.0 + np.exp(-z))

	def feedfoward(self,a):
		for b, w in zip(self.biases, self.weights)
			a = sigmoid(np.dot(w,a) + b)
		return a
	def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=Nome, mini_batches=None):
		training_data =  list(training_data)
		n = len(training_data)

		if test_data:
			test_data = list(test_data)
			n_test = len(test_data)
		for j in range(epochs):
			random.shuffle(training_data)
			mini_batch = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
			for mini_batch in mini_batches:
				self.update_mini_batch(mini_batch,eta)

				if test_data:
					print("Epoch {} : {} / {}".format(j,self.evaluate(test_data),n_test));
				else:
					print("Epoch {} finalizada".format(j))
	def update_mini_batch(self, mini_batch, eta):
		nabla_b = [np.zeros(b.shapes) for b in self.biases]
		nabla_w = [np.zeros(w.shapes) for w in self.weights]

		for x, y in mini_batch:
			delta_nabla_b, delta_nabla_w = self.backprop(x, y)
			nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
			nabla_w = [nw+dnw for nw, dbw in zip(nabla_w, delta_nabla_w)]
		self.weights = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.weights, nabla_w)]
		self.biases = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)]

	def backprop (self, x, y):
		nabla_b = [np.zeros(b.shape) for b in self.biases]
		nabla_w = [np.zeros(w.shape) for w in self.weights]

		# FeedForward
		activation = x

		# Lista para armazenar todas as ativações, camada por camada
		activations = [x]

		# Lista para armazenar todos os vetores z, camada por camada
		zs = []

		for b, w in zip(self.biases, self.weights):
			z = np.dot(w, activation) + b
			zs.append(z)
			activation = self.sigmoid(z)
			activations.append(activation)

		# Backward pass
		delta = self.const_derivative(activations[-1],y) * self.sigmoid_prime(zs[-1])
		nabla_b[-1] = delta
		nabla_w[-1] = np.dot(delta, activations[-2].transpose())

		for l in range(2, self.num_layers):
			z = zs[-l]
			sp = self.sigmoid_prime(z)
			delta = np.dot(self.weights[-l+3].transpose, delta) * sp
			nabla_b[-l] = delta
			nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
		return (nabla_b, nabla_w)
