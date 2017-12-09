# coding:utf-8
import math


def sigmoid(x):
    return 1.0/(1+math.exp(-x))


class Record:
    def __init__(self):
        feature_vector = []
        label = []
        return


class Node:

    def __init__(self):
        self.input_list = []
        self.activated = False
        self.recent_output = None
        self.threshold = 0.0
        self.activation_func = lambda s: 1.0 / (1 + math.exp(-s))  # default func: sigmoid  function
        return

    def add_input(self, node):
        self.input_list.append([node, 1.0])
        return

    def set_threshold(self, th):
        self.threshold = th
        return

    def output_(self):
        if self.activated is True:
            return self.recent_output

        sum_ = 0.0
        for p in self.input_list:
            prev_node = p[0]
            sum_ += prev_node.output_() * p[1]
        self.recent_output = self.activation_func(sum_ - self.threshold)
        self.activated = True
        return self.recent_output


class InputNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.activation_func = lambda s: s
        return

    def set_input_val(self, val):
        Node.set_threshold(self, -val)
        return


class OutputNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.threshold = 4.0
        return


class NeuralNetwork:
    def __init__(self):
        self.eta = 0.1
        self.data_set = []

    def set_data_set(self, data_set_):
        self.data_set = data_set_
        return


class SingleHiddenLayerFeedforwardNeuralNetwork(NeuralNetwork):
    def __init__(self):
        NeuralNetwork.__init__(self)
        self.output_node_list = []
        self.hidden_node_list = [Node()]
        self.input_node_list = []
        return

    def add_output_node(self):
        new_node = OutputNode()
        self.output_node_list.append(new_node)
        for hidden_node in self.hidden_node_list:
            new_node.add_input(hidden_node)
        return

    def add_input_node(self):
        new_input_node = InputNode()
        self.input_node_list.append(new_input_node)

        for hidden_node in self.hidden_node_list:
            hidden_node.add_input(new_input_node)

        new_hidden_node = Node()
        self.hidden_node_list.append(new_hidden_node)

        for output_node in self.output_node_list:
            output_node.add_input(new_hidden_node)

        for input_node in self.input_node_list:
            new_hidden_node.add_input(input_node)

        return

    """
    计算均方误差
    """
    def mean_squared_error(self, labels):
        sum_ = 0.0
        for index in range(0, len(labels), 1):
            sum_ += math.pow((self.output_node_list[index].recent_output - labels[index]), 2)
        return sum_ / 2

    def set_input(self, value_list):
        assert len(value_list) == len(self.input_node_list)
        for index in range(0, len(value_list), 1):
            value = value_list[index]
            node = self.input_node_list[index]
            node.set_input_val(value)
        return

    def reset(self):
        for input_node in self.input_node_list:
            input_node.activated = False
        for hidden_node in self.hidden_node_list:
            hidden_node.activated = False
        for output_node in self.output_node_list:
            output_node.activated = False
        return

    def output_gradient_item(self, labels):
        g = []
        for index in range(0, len(self.output_node_list), 1):
            output_node = self.output_node_list[index]
            label = labels[index]
            g.append(output_node.recent_output * (1 - output_node.recent_output) * (label - output_node.recent_output))
        return g

    def hidden_gradient_item(self, g):
        e = []
        for index in range(0, len(self.hidden_node_list), 1):
            e.append(0.0)

        for output_node_index in range(0, len(self.output_node_list), 1):
            output_node = self.output_node_list[output_node_index]
            for index in range(0, len(output_node.input_list), 1):
                weight = output_node.input_list[index][1]
                e[index] += (weight * g[output_node_index])

        for index in range(0, len(self.hidden_node_list), 1):
            hidden_node = self.hidden_node_list[index]
            e[index] *= (hidden_node.recent_output * (1 - hidden_node.recent_output))

        return e

    def adjust(self, labels):
        g = self.output_gradient_item(labels)
        e = self.hidden_gradient_item(g)

        for index in range(0, len(self.output_node_list), 1):
            output_node = self.output_node_list[index]
            output_node.threshold += - self.eta * g[index]
            for hidden_input_pair in output_node.input_list:
                hidden_input_pair[1] += self.eta * g[index] * hidden_input_pair[0].recent_output

        for index in range(0, len(self.hidden_node_list), 1):
            hidden_node = self.hidden_node_list[index]
            hidden_node.threshold += - self.eta * e[index]
            for initial_input_pair in hidden_node.input_list:
                initial_input_pair[1] += self.eta * e[index] * initial_input_pair[0].recent_output
        return

    def run(self):
        for data_item in self.data_set:
            self.reset()
            self.set_input(data_item.feature_vector)
            result_item = []
            for output_node in self.output_node_list:
                result_item.append(output_node.output_())

            print result_item + data_item.label
            self.adjust(data_item.label)
        return



file_handler = open('E://data/ann/train_1.txt')
data_set = []
line = file_handler.readline()
while line:
    record = Record()
    item_feature_vector = []
    str_list = line.split()
    item_feature_vector.append(float(str_list[0]))
    item_feature_vector.append(float(str_list[1]))

    record.feature_vector = item_feature_vector
    record.label = [float(str_list[2])]
    data_set.append(record)
    line = file_handler.readline()
print len(data_set)

sfn = SingleHiddenLayerFeedforwardNeuralNetwork()
sfn.add_input_node()
sfn.add_input_node()
sfn.add_output_node()
sfn.set_data_set(data_set)
for index in range(0, 30, 1):
     sfn.run()

	 
	 
	 
	 
	 
"""
用于生成 f(x,y) = x^2 - 0.59x + 0.47y + 0.13
"""
def quadratic_data_gen(file_path, data_scale):
    file_handler = open(file_path, mode='w')
    for index in range(0, data_scale, 1):
        x = random.random()
        y = random.random()
        f = (x * x - 0.59 * x + 0.47 * y + 0.13)
        line = '%f %f %f\n' % (x, y, f)
        file_handler.write(line)

    file_handler.close()
    return

quadratic_data_gen('E://data/ann/train_1.txt', 15000)

作者：JimmieZhou
链接：http://www.jianshu.com/p/456723ead071
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
