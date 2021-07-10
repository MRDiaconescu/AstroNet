
'''
builder version 1.1, 10 July 2021
author: Maria Raluca Diaconescu
the program creates a social network using data 
that the user can find in the application

'''

import datetime

from datetime import date

from datetime import date as date_module







print("Welcome to astro net!")
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







class AstroNet():

	class Sphere(): 

		def __init__(self, coordinate=77, link1=1, link2=2, link3=3, link4=4, link5=5, link6=6, link7=7,
			link8=8, link9=9, link10=10, link11=11, link12=12, link15=15, link17=17, link25=25):

			self.coordinate = coordinate;

			self.link1 = link1;
			self.link2 = link2;
			self.link3 = link3;
			self.link4 = link4;
			self.link5 = link5;
			self.link6 = link6;
			self.link7 = link7;
			self.link8 = link8;
			self.link9 = link9;
			self.link10 = link10;
			self.link11 = link11;
			self.link12 = link12;
			self.link15 = link15;
			self.link17 = link17;
			self.link25 = link25;
	

		class Account(object):



			def __init__(self, name,  date_of_birth, country, friends, account_link1=1, account_link2=2):

				self.profile = {'name':name, 'date_of_birth':date_of_birth, "country":country}
				self.friends = [friends]
				self.settings = {'private_profile':False, 'receive_messages':True, 'receive_emails':True}
				self.session = None #{active:yes}

				self.account_link1 = account_link1;
				self.account_link2 = account_link2; 



			def build_profile(self, name, date_of_birth, country):

				self.profile['name'] = name
				self.profile['date_of_birth'] = date_of_birth
				self.profile['country'] = country

				print(self.profile['name'])



			def edit_settings(self, name, date_of_birth, country, friends, settings_link1=1, settings_link2=2):


				class Settings(AstroNet.Sphere.Account):

					settings_var = {'private_profile':False, 'receive_messages':True, 'receive_emails':True}


					def __init__(self): 

						self.settings = Settings.settings_var 

						AstroNet.Sphere.Account.__init__(self, name, date_of_birth, country, friends)

						self.settings_link1 = settings_link1;
						self.settings_link2 = settings_link2;

					def edit_privacy_settings(self, arg):

						Settings.settings_var['private_profile'] = arg

						AstroNet.Sphere.Account.settings = self.settings = Settings.settings_var

						print("var1:", AstroNet.Sphere.Account.settings)

						print("var2:", self.settings)

						return AstroNet.Sphere.Account.settings, self.settings


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



		class Person():

			def __init__(self):

				self.centralized_database = [[[]for i in range(5)] for m in range(5)]

			def centralized_database_f1(self):

				return self.centralized_database

			def add_person_to_centralized_database(self, arg1):

				counter = 0

				for item in range(len(self.centralized_database)):

					for item1 in range(len(self.centralized_database[item])):

						if self.centralized_database[item][item1] == []:


							if counter == 1:

								break

							
							counter+=1

							self.centralized_database[item][item1] = arg1


						

				return self.centralized_database




		class Message(Account):

			def __init__(self, arg1, title, message_content, message_link1=1, message_link2=2):

				self.friends = arg1.friends

				self.messages = [ [dict({})] for item in range(len(arg1.friends))]

				self.message_text = {'Title':title, 'Message_content':message_content}

				self.message_link1 = message_link1;

				self.message_link2 = message_link2;


			def send_message_to_a_friend_from_the_same_network(self, arg1, arg2):

				counter = 0

				if (arg2 in arg1.friends):

					counter+=1

					arg2=counter

					self.messages.append(self.message_text)

				else:

					print(arg2 + " is not a member of your friends network.")
					answer = input("Would you like to add " + arg2 + " to your friends network? ")



				return self.messages





		class Friend(Account):

			def __init__(self, name, date_of_birth, country, friends, friend_link1=1, friend_link2=2):

				#the attributes from the __init__ method of account are inherited

				super(AstroNet.Sphere.Friend,self).__init__(name, date_of_birth, country, friends) 

				self.friend_link1 = friend_link1;

				self.friend_link2 = friend_link2;



			def add_friends_from_the_same_network(self, name, date_of_birth, country, friends):
				
					#class which calls another class which calls another class

					#using specific attributes from the initial class

					class Friends_network(AstroNet.Sphere.Friend):


						def __init__(self, friends_network_link1=1, friends_network_link2=2):
							
							AstroNet.Sphere.Friend.__init__(self, name, date_of_birth, country, friends)

							self.friends_network_link1 = friends_network_link1;

							self.friends_network_link2 = friends_network_link2;

							self.friends.append(self.profile['name'])

							for item in self.friends:

								print (item)



						def display_friends_list(self):

							return self.friends


					

					friends_network = Friends_network()

					return friends_network



				

			def add_friends(self, name, date_of_birth, country, friends):

				class Friends_network(AstroNet.Sphere.Friend):

					def __init__(self, friends_network_link1=1, friends_network_link2=2):
						
						AstroNet.Sphere.Friend.__init__(self, name, date_of_birth, country, friends)

						self.friends_network_link1 = friends_network_link1;

						self.friends_network_link2 = friends_network_link2;

						self.friends.append(name)

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

			def __init__(self, data, adjVertex_link1=1, adjVertex_link2=2):

				self.vertex = data
				self.next = None
				self.adjVertex_link1 = adjVertex_link1;
				self.adjVertex_link2 = adjVertex_link2;
		    


		class Graph():

			def __init__(self, vertices, graph_link1=1, graph_link2=2):

				self.V = vertices
				self.graph = [None] * self.V
				self.graph_link1 = graph_link1;
				self.graph_link2 = graph_link2;


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

			def __init__(self, cell=7, shell=77, medium=777, link1=1, link2=2, link5=5, link7=7, builder_link1=1, builder_link2=2):

				self.counter=0

				self.network = {}

				self.level_counter = 0

				self.builder_link1=builder_link1;

				self.builder_link2 = builder_link2;

			
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

				return  arg1#(self.counter,arg1)


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

				return (self.counter, AstroNet().Sphere().AdjVertex(vertex_var))



			def vertex_f1(self, var1, var2, var5, var7, var11, var15, var17):

				return var1.instance_f1(var2, var5, var7, var11, var15, var17)





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

					if type(i) == AstroNet.Sphere.AdjVertex:

						var_vertex_list1.append(i)

					if type(i) == list:

						for item in range(len(i)):

							if type(i[item]) != list:
								
								print(i[item].__dict__)

								var_vertex_list1.append(i[item])


				return var_vertex_list1



			def create_a_graph(self, args_list):

				var_graph = AstroNet().Sphere().Graph(len(args_list))

				var_graph_list = []

				for item in range(len(args_list)):

					var_graph.add_edge_f1_2(var_graph, args_list[0], args_list[item])
					
					print(args_list[0].next)

					print(args_list[0].next.__dict__)

					var_graph_list.append(args_list[0].next)

					var_graph.graph = var_graph_list

				return (var_graph, var_graph_list)



			def display_the_graph(self, arg1):

				for item in arg1.__dict__['graph']:

					print(item)

					if item != None:

						print(item.__dict__)


			def create_networks(self, arg1, arg2, arg5):

				print("Graph")

				args_list = []

				var_graph_list = []

				for item in arg1.create_a_vertex_list_f1(arg2):
					
					print(item)
					print(item.__dict__)

					for item1 in  arg1.create_a_vertex_list_f1(arg5):
						
						print(item1)
						print(item1.__dict__)

						if item.__dict__['vertex']['name'] == item1.__dict__['vertex']['name']:

							args_list.append(item)

				var_graph = AstroNet().Sphere().Graph(len(args_list))

				for item in range(len(args_list)):
					
				    print(args_list[item].__dict__)

				    var_graph.add_edge_f1_2(var_graph, args_list[0], args_list[item])
					
				    print(args_list[0].next)

		    		    print(args_list[0].next.__dict__)

				    var_graph_list.append(args_list[0].next)

				    var_graph.build_graph(args_list[0].next)


				return var_graph



			def add_a_friend_to_the_joined_network(self, arg1, arg2):

				for item in arg1.graph: 
				
					if arg2 not in arg1.graph:

						arg1.build_graph(arg2)

				return arg1.graph



			def find_friends_of_friends(self, arg1):

				print("First", vertex1_1[1].__dict__['friends'][1])
				print("First", vertex1_1[1].__dict__['friends'][1].__dict__)


				var_1st_level = ("First level", arg1[1].__dict__['friends'][1])

				var_initial_level = []

				var_friends_of_friends = []

				var_initial_level.append(var_1st_level)

				for item in arg1[1].__dict__['friends'][0]:

					print(item)

					if type(item) != list:

						print("Second", item.__dict__)

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

								print("Third", item1.__dict__)

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


			def __init__(self, name, date_of_birth, country, friends, first_link1=1, first_link2=2):

				#the attributes from the __init__ method of account are inherited

				super(AstroNet.Sphere.First,self).__init__(name, date_of_birth, country, friends) 

				self.first_link1 = first_link1;

				self.first_link2 = first_link2;



			def add_friends_from_the_same_network(self, name, date_of_birth, country, friends, arg1, arg2):

				    class Friends_network(AstroNet.Sphere.Friend):

			    		 def __init__(self, friends_network_link1=1, friends_network_link2=2):

			    		 	AstroNet.Sphere.Friend.__init__(self, name, date_of_birth, country, friends)

			    		 	self.friends_network_link1 = friends_network_link1;

			    		 	self.friends_network_link2 = friends_network_link2;

			    		    #the attributes of Friend are accessed through the Account class


			    		 	self.f1 = AstroNet.Sphere.Builder.f1


			    		 	if self.f1(self, arg1, arg2, self.profile['name']):

			    		 		self.friends.append(self.profile['name'])

			    		 		for item in self.friends:

			    		 			print(item)

					
				    friends_network = Friends_network()

				    return friends_network




		class First_message(Account):

			def __init__(self, arg1, title, message_content, message_link1=1, message_link2=2):

				self.friends = arg1.friends

				self.messages = [ [dict({})] for item in range(len(arg1.friends))]

				self.message_text = {'Title':title, 'Message_content':message_content}

				self.message_link1 = message_link1;

				self.message_link2 = message_link2;


			def add_friend_f1(self):

				date_of_birth=input("Enter a date in the format yyyy-mm-dd ")

				date_of_birth = date_module.fromisoformat(date_of_birth)

				return date_of_birth

			def add_friend_f1_1(self):

				country = input("Enter the country name ")

				return country

			def centralized_database_f1_1(self, arg1):

				date_of_birth = self.add_friend_f1()
				country = self.add_friend_f1_1()

				for item in arg1.centralized_database:

						 print(item)

						 print(type(item))

						 for item1 in item:

						 	if type(item1) != list:

							 	if ((item1.profile['date_of_birth'] == date_of_birth) and (item1.profile['country']==country)):

							 		print(item1)

							 		return item1

						 	else:

						 		pass



			def send_message_to_a_friend_from_the_same_network_f1(self, arg1, arg2):

				counter = 0

				if (arg2.profile['name'] in arg1.friends):

					counter+=1

					#arg2=counter

					self.messages.append(self.message_text)

				else:

					print(arg2.profile['name'] + " is not a member of your friends network.")
					answer =input("Would you like to add " + arg2.profile['name'] + " to your friends network? Type yes or no ")

					print("True")

					if (answer == "yes"):

						friends_list = arg1.add_friends(arg2, arg2.profile['date_of_birth'], arg2.profile['country'], arg2.friends)

						print(arg2.profile['name'] + " is now your friend ")

						arg1.friends.append(friends_list)



				return (self.messages, arg1)





		class NestCell(Builder):


			def __init__(self, cell, shell, medium, link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2):

				self.cell = cell
				self.shell = shell
				self.medium = {medium}

				self.link1 = link1
				self.link2 = link2
				self.link5 = link5
				self.link7 = link7

				self.nestCell_link1 = nestCell_link1;
				self.nestCell_link2 = nestCell_link2;

				#the attributes from the __init__ method of Builder are inherited

				super(AstroNet.Sphere.NestCell, self).__init__(cell, shell) 


			class Gate1():

				def __init__(self, gate1_link1=1, gate1_link2=2):

					self.gate1_link1 = gate1_link1;

					self.gate1_link2 = gate1_link2;


				def build_the_nest_cell(self, cell, shell, medium, link1=1, link2=2, link5=5, link7=7):

					class NestingHive(AstroNet.Sphere.NestCell):

						def __init__(self, nestingHive_link1=1, nestingHive_link2=2):

							#to access 

							AstroNet.Sphere.NestCell.__init__(self, cell, shell, medium)

							self.nestingHive_link1 = nestingHive_link1;

							self.nestingHive_link2 = nestingHive_link2;

							
							#the attributes of NestCell are accessed through the Builder class

						def build_the_hive_1(self, arg1):

							for item in arg1:

								self.medium.add(item)

							return self		

						def build_the_hive_2(self, arg1):

							self.link1 = arg1

							return self


						def build_the_hive_2_1(self, arg2):

							self.link2 = arg2

							return self

						def build_the_hive_5_1(self, arg5):

							self.link5 = arg5

							return self

						def build_the_hive_7_1(self, arg7):

							self.link7 = arg7

							return self

						def NestingHive_function(self, arg, arg1, arg2, arg5, arg7):

							arg.build_the_hive_2(arg1)
							arg.build_the_hive_2_1(arg2)
							arg.build_the_hive_5_1(arg5)
							arg.build_the_hive_7_1(arg7)

							return arg

						def canal(self):

							return AstroNet().Sphere().NestCell(self, cell, shell, medium).Gate1().build_the_nest_cell(self, cell, shell, medium)


					the_hive = NestingHive()

					return the_hive

			
			class Gate2():

				def __init__(self, gate2_link1=1, gate2_link2=2):

					self.gate2_link1 = gate2_link1;

					self.gate2_link2 = gate2_link2;

				def path_function(self, cell, shell, medium, link1=1, link2=2, link5=5, link7=7):

					return AstroNet().Sphere().NestCell(cell, shell, medium).Gate1().build_the_nest_cell(self, cell, shell, medium).canal()


		def connect(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg15, arg17, arg25):

			self.link1 = arg1;
			self.link2 = arg2;
			self.link3 = arg3;
			self.link4 = arg4;
			self.link5 = arg5;
			self.link6 = arg6;
			self.link7 = arg7;
			self.link8 = arg8;
			self.link9 = arg9;
			self.link10 = arg10;
			self.link11 = arg11;
			self.link12 = arg12;
			self.link15 = arg15;
			self.link17 = arg17;
			self.link25 = arg25;

			return self





		


AstroNet.Sphere.AdjVertex.add_friends_from_the_same_network = AstroNet.Sphere.Friend.add_friends_from_the_same_network

AstroNet.Sphere.AdjVertex.builder_function = AstroNet.Sphere.Builder.builder_function

AstroNet.Sphere.AdjVertex.friends = []

AstroNet.Sphere.AdjVertex.add_friends = AstroNet.Sphere.Friend.add_friends

AstroNet.Sphere.AdjVertex.builder_function_1 = AstroNet.Sphere.Builder.builder_function_1

AstroNet.Sphere.AdjVertex.builder_function_2 = AstroNet.Sphere.Builder.builder_function_2

AstroNet.Sphere.AdjVertex.builder_function_5 = AstroNet.Sphere.Builder.builder_function_5




AstroNet.Sphere.First.add_friends = AstroNet.Sphere.Friend.add_friends

AstroNet.Sphere.First.add_yourself_to_the_list_of_friends = AstroNet.Sphere.Friend.add_yourself_to_the_list_of_friends


