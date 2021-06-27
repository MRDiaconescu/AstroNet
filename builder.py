'''
builder version 1.0, 20 June 2021
author: Maria Raluca Diaconescu
the program creates a social network using data 
that the user can find in the application

'''



import datetime

from datetime import date





print("Welcome to AstroNet!")
print("                                     *                                            ")
print("                                    * *                                           ")
print("                                   *   *                                          ")
print("                                  *     *                                         ")
print("                                 *       *                                        ")
print("                                *         *                                       ")
print("                               *           *                                      ")
print("                              *             *                                     ")
print("                             *               *                                    ")
print("                            *                 *                                   ")
print("   *   *   *   *   *    *                       *   *   *   *   *   *   *  *      ")
print("     *                                                                  *         ")
print("       *                                                              *           ")
print("        *                                                           *             ")
print("          *                                                       *               ")
print("            *                                                   *                 ")
print("              *                                               *                   ")
print("                *                                           *                     ")
print("                  *                                       *                       ")
print("                  *                                       *                       ")
print("                 *                                         *                      ")
print("                *                                           *                     ")
print("               *                     *                       *                    ")
print("              *                 *         *                   *                   ")
print("             *              *                 *                *                  ")
print("            *           *                         *             *                 ")
print("           *        *                                 *          *                ")
print("          *     *                                         *       *               ")
print("         *   *                                                *    *              ")
print("        * *                                                       * *             ")





class Account(object):



	def __init__(self, name,  date_of_birth, country, friends):

		self.profile = {'name':name, 'date_of_birth':date_of_birth, "country":country}
		self.friends = [friends]
		self.settings = {'private_profile':False, 'receive_messages':True, 'receive_emails':True}
		self.session = None 


	def build_profile(self, name, date_of_birth, country):

		self.profile['name'] = name
		self.profile['date_of_birth'] = date_of_birth
		self.profile['country'] = country

		print(self.profile['name'])




	def edit_settings(self, name, date_of_birth, country, friends):


		class Settings(Account):

			settings_var = {'private_profile':False, 'receive_messages':True, 'receive_emails':True}


			def __init__(self): 

				self.settings = Settings.settings_var 

				Account.__init__(self, name, date_of_birth, country, friends) 


			def edit_privacy_settings(self, arg):

				Settings.settings_var['private_profile'] = arg

				Account.settings = self.settings = Settings.settings_var

				return Account.settings, self.settings


			def message_box_settings(self, arg1):

				Settings.settings_var['receive_messages'] = arg1

				self.settings = Settings.settings_var

				return self.settings


			def mail_settings(self, arg2):

				Settings.settings_var['receive_mails'] = arg2

				self.settings = Settings.settings_var

				return self.settings




		settings_var1 = Settings() 

		return settings_var1





class Message(Account):

	def __init__(self, arg1, title, message_content):

		self.friends = arg1.friends

		self.messages = [ [dict({})] for item in range(len(arg1.friends))]

		self.message_text = {'Title':title, 'Message_content':message_content}


	def send_message_to_a_friend_from_the_same_network(self, arg1, arg2):

		counter = 0

		if (arg2 in arg1.friends):

			counter+=1

			arg2=counter

			self.messages[arg2] = self.message_text

		else:

			print(arg2 + " is not a member of your friends network.")
			answer = input("Would you like to add " + arg2 + " to your friends network?")

		return self.messages





class Friend(Account):

	def __init__(self, name, date_of_birth, country, friends):

		super(Friend,self).__init__(name, date_of_birth, country, friends) 

		print(self.friends)


	def add_friends_from_the_same_network(self, name, date_of_birth, country, friends):

			class Friends_network(Friend):

				def __init__(self):

					Friend.__init__(self, name, date_of_birth, country, friends)

					self.friends.append(self.profile['name'])

					print("Friends list: ", self.friends)

					for item in self.friends:

						print (item)



				def display_friends_list(self):


					return self.friends


			

			friends_network = Friends_network()

			return friends_network



		

	def add_friends(self, name, date_of_birth, country, friends):

		class Friends_network(Friend):


			def __init__(self):
				
				Friend.__init__(self, name, date_of_birth, country, friends)

				self.friends.append(self.profile['name'])

				print("Friends list: ", self.friends)

				for item in self.friends:

					print (item)



			def display_friends_list(self):

				return self.friends


		friends_network = Friends_network()

		return friends_network



	def add_yourself_to_the_list_of_friends(self):

		self.friends.add(self.profile['name'])

		print(self.friends)	


  
class AdjVertex():

	def __init__(self, data):

		self.vertex = data
		self.next = None
    


class Graph():

	def __init__(self, vertices):

		self.V = vertices
		self.graph = [None] * self.V


	def add_edge(self, src, dest):

		vertex = AdjVertex(dest)
		vertex.next = self.graph[src]
		self.graph[src] = vertex

		vertex = AdjVertex(src)
		vertex.next = self.graph[dest]
		self.graph[dest] = vertex


	def add_edge_f1_1(self, src, dest):

		src.next = dest
		dest.next = src


	def add_edge_f1(self, arg1, arg2, arg5):

		return arg1.add_edge(arg2, arg5)


	def add_edge_f1_2(self, arg1, arg2, arg5):

		return arg1.add_edge_f1_1(arg2, arg5)


	def build_graph(self, arg1):

		self.graph.append(arg1)






class Builder():

	def __init__(self):

		self.counter=0

		self.network = {}

		self.level_counter = 0

	
	def build_the_friend_network_f1_A(self, arg1, arg2, arg3, arg5):

		arg1.friends = arg1.add_friends_from_the_same_network(arg2, arg3, arg5, arg1.friends).friends

		return arg1.add_friends_from_the_same_network(arg1, arg2, arg5, arg1.friends).friends



	def build_the_friend_network_f1_1_A(self, arg1, arg2, arg3, arg5):

		arg1.friends = arg1.add_friends_from_the_same_network(arg2, arg3, arg5, arg1.friends).friends

		return arg1.add_friends_from_the_same_network(arg1, arg2, arg5, arg1.friends).friends



	def build_the_friend_network_f1_B(self, arg1, arg2, arg3, arg5):

		arg1.friends = arg1.add_friends(arg2, arg3, arg5, arg1.friends).friends

		return arg1.add_friends(arg1, arg2, arg5, arg1.friends).friends



	def instance_f1(self,arg1, arg2, arg3, arg5, arg6, arg7):

		arg1 = arg2(arg3, arg5, arg6, arg7)

		return  arg1


	def builder_function(self,arg1, arg2, arg3,arg5, arg6):

		self.level_counter+=1

		return arg1.build_the_friend_network_f1_A(arg2, arg3, arg5, arg6)



	def builder_function_1(self,arg1, arg2, arg3,arg5, arg6):

		self.level_counter+=1

		return arg1.build_the_friend_network_f1_1_A(arg2, arg3, arg5, arg6)


	def builder_function_2(self,arg1, arg2, arg3,arg5, arg6):

		self.level_counter+=1

		return arg1.build_the_friend_network_f1_1_A(arg2, arg3, arg5, arg6)


	def builder_function_5(self,arg1, arg2, arg3,arg5, arg6):

		self.level_counter+=1

		return arg1.build_the_friend_network_f1_B(arg2, arg3, arg5, arg6)



	def vertex(self, arg1):

		self.counter+=1

		name_var = arg1.profile['name']

		date_of_birth_var = arg1.profile['date_of_birth']

		country_var = arg1.profile['country']

		friends_list = arg1.friends

		vertex_var = {'name':name_var, 'date_of_birth': date_of_birth_var, 'country':country_var, 'friends':friends_list}

		return (self.counter, AdjVertex(vertex_var))



	def vertex_f1(self, var1, var2, var5, var7, var11, var15, var17):

		return var1.instance_f1(var2, var5, var7, var11, var15, var17)


	def create_a_vertex_list(self, arg1):

		var_vertex_list = []

		var_vertex_list.append(arg1[1])

		for item in arg1[1].__dict__['friends']:

			if type(item) ==  list:

				for item1 in item:

					var_vertex_list.append(item1)


			if type(item) != list:

				var_vertex_list.append(item)



		return var_vertex_list





	def create_a_vertex_list_f1(self, arg1):

		var_vertex_list = []

		var_vertex_list1 = []

		var_vertex_list.append(arg1[1])

		for item in arg1[1].__dict__['friends']:

			if type(item) ==  list:

				for item1 in item:

					var_vertex_list.append(item1)


			if type(item) != list:

				var_vertex_list.append(item)


		for i in var_vertex_list:

			if type(i) == AdjVertex:

				var_vertex_list1.append(i)

			if type(i) == list:

				for item in range(len(i)):

					if type(i[item]) != list:

						print(i[item].__dict__)

						var_vertex_list1.append(i[item])


		return var_vertex_list1



	def create_a_graph(self, args_list):

		var_graph = Graph(len(args_list))

		for item in range(len(args_list)):

			var_graph.add_edge_f1_2(var_graph, args_list[0], args_list[item])

			var_graph.build_graph(args_list[0].next)

		return var_graph



	def display_the_graph(self, arg1):

		for item in arg1.__dict__['graph']:

			print(item)

			if item != None:

				print(item.__dict__)




	def find_friends_of_friends(self, arg1):


		var_1st_level = ("First level", arg1[1].__dict__['friends'][1])

		var_initial_level = []

		var_friends_of_friends = []

		var_initial_level.append(var_1st_level)

		for item in arg1[1].__dict__['friends'][0]:

			print(item)

			if type(item) != list:

				if ('vertex' in item.__dict__ and 'friends' in item.__dict__['vertex']
				and 'friends' not in item.__dict__):

					for friend in item.__dict__['vertex']['friends']:

						var_initial_level.append(("Second level", friend))

				elif 'friends' in item.__dict__:

					for friend in item.__dict__['friends']:

						var_initial_level.append(("Second level", friend))


			else: 

				for item1 in item:

					if type(item1) != list:

						var_initial_level.append(("Third level:", item1))

						if ('vertex' in item1.__dict__ and 'friends' in item1.__dict__['vertex'] 
						and 'friends' not in item1.__dict__):
									
							for friend1 in item1.__dict__['vertex']['friends']:

								var_friends_of_friends.append(friend1)

								var_initial_level.append(("Third level", friend1))

						if ('vertex' in item1.__dict__ and 'friends' in item1.__dict__['vertex'] 
						and 'friends' in item1.__dict__):

							for friend1 in item1.__dict__['friends']:

								if type(friend1) != list:

									var_friends_of_friends.append(friend1)

									var_initial_level.append(("Third level", friend1))


								else:

									pass


									
			
		return  (var_initial_level, var_friends_of_friends)




	def display_friends_of_friends(self,arg1):

		for item in arg1[1]:

			print(item.__dict__)


	def f1(self, arg1, arg2, arg3 ):

		for item in arg1.find_friends_of_friends(arg2)[1]:

			if arg3[1] == item:

				return True


	def f2(self, var1, arg1, arg2, arg3, arg5, arg7):

		if var1 == True:

			return arg1.builder_function_1(arg1, arg2, arg3, arg5, arg7)


	def f2_1(self, var1, arg1, arg2, arg3, arg5, arg7):

		if var1 == True:

			Friend.add_friends_from_the_same_network = First.add_friends_from_the_same_network

			return arg1.builder_function_1(arg1, arg2, arg3, arg5, arg7)


	def f5(self, var1, arg1, arg2, arg3, arg5, arg7):

		if var1 == True:

			return arg1.builder_function_5(arg1, arg2, arg3, arg5, arg7)






class First(Account):


	def __init__(self, name, date_of_birth, country, friends):

		super(First,self).__init__(name, date_of_birth, country, friends) 

		print(self.friends)


	def add_friends_from_the_same_network(self, name, date_of_birth, country, friends, arg1, arg2):

		    class Friends_network(Friend):

	    		 def __init__(self):

	    		 	Friend.__init__(self, name, date_of_birth, country, friends) 
	    		 	self.f1 = Builder.f1


	    		 	if self.f1(self, arg1, arg2, self.profile['name']):

	    		 		self.friends.append(self.profile['name'])

	    		 		for item in self.friends:

	    		 			print(item)

			
		    friends_network = Friends_network()

		    return friends_network





	


AdjVertex.add_friends_from_the_same_network = Friend.add_friends_from_the_same_network

AdjVertex.builder_function = Builder.builder_function

AdjVertex.friends = []

AdjVertex.add_friends = Friend.add_friends

AdjVertex.builder_function_1 = Builder.builder_function_1

AdjVertex.builder_function_2 = Builder.builder_function_2

AdjVertex.builder_function_5 = Builder.builder_function_5




First.add_friends = Friend.add_friends

First.add_yourself_to_the_list_of_friends = Friend.add_yourself_to_the_list_of_friends



