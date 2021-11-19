
'''
builder version 3.0, 18 November 2021
author: Maria Raluca Diaconescu
the program creates a social network using data 
that the user can find in the application

'''

import datetime

from datetime import date

from datetime import date as date_module






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







class AstroNet():

	class Sphere(): 

		def __init__(self, coordinate=77,link1=1, link2=2, link3=3, link4=4, link5=5, link6=6, link7=7,
			link8=8, link9=9, link10=10, link11=11, link12=12, link15=15, link17=17, link25=25, communications_list="communications list" ):

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

			self.primary_memory = ["LinkedlList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
			                      "Builder", "First", "First_message", "NestCell"]
			self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]

			self.communications_list = communications_list

		class Data():

			def __init__(self, value=1, info="data"):

				self.value = value

				self.info = info


		def HiveCell_f1(self, value=1, info="data", link_node=True, instance="instance", hive_cell_message="hive_cell message"):

			class HiveCell(AstroNet.Sphere):
				
				def __init__(self, value, info, instance="instance", link_node=True):

					AstroNet.Sphere.__init__(self)

					self.value = value

					self.link_node = link_node

					self.info = info

					self.hive_cell_message = hive_cell_message

					self.instance = instance
				
				def set_link_node(self, link_node): self.link_node = link_node;

				def set_link_node1(self, link_node): self.link_node = link_node;

				def set_link_node2(self, link_node): self.link_node = link_node;

				def set_link_node3(self, link_node): self.link_node = link_node;

				def set_link_node4(self, link_node): self.link_node = link_node;

				def set_link_node5(self, link_node): self.link_node = link_node;

				def set_link_node6(self, link_node): self.link_node = link_node;

				def set_link_node7(self, link_node): self.link_node = link_node;

				def set_link_node8(self, link_node): self.link_node = link_node;

				def set_link_node9(self, link_node): self.link_node = link_node;

				def set_link_node10(self, link_node): self.link_node = link_node;

				def set_link_node11(self, link_node): self.link_node = link_node;

				def set_link_node12(self, link_node): self.link_node = link_node;

				def set_link_node13(self, link_node): self.link_node = link_node;

				def set_link_node14(self, link_node): self.link_node = link_node;

				def set_link_node15(self, link_node): self.link_node = link_node;

				def set_link_node16(self, link_node): self.link_node = link_node;

				def set_link_node17(self, link_node): self.link_node = link_node;

				def set_link_node18(self, link_node): self.link_node = link_node;

				def set_link_node19(self, link_node): self.link_node = link_node;

				def set_link_node20(self, link_node): self.link_node = link_node;

				def set_link_node21(self, link_node): self.link_node = link_node;

				def set_link_node22(self, link_node): self.link_node = link_node;

				def set_link_node23(self, link_node): self.link_node = link_node;

				def set_link_node24(self, link_node): self.link_node = link_node;

				def set_link_node25(self, link_node): self.link_node = link_node;

				def set_link_node26(self, link_node): self.link_node = link_node;

				def set_link_node27(self, link_node): self.link_node = link_node;

				def set_link_node28(self, link_node): self.link_node = link_node;

				def set_link_node29(self, link_node): self.link_node = link_node;

				def set_link_node30(self, link_node): self.link_node = link_node;

				def set_link_node31(self, link_node): self.link_node = link_node;

				def set_link_node32(self, link_node):self.link_node = link_node;

				def get_link_node(self):

					return self.link_node


			var_hive_cell = HiveCell(value, info)

			return var_hive_cell
		


		class LinkedList():


				def __init__(self, value, info, linked_list_message="linked_list message"):

					self.head_node = AstroNet().Sphere().HiveCell_f1(value, info)

					self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
											"Builder", "First", "First_message", "NestCell"]
					self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]

					self.linked_list_message = "linked_list message"

				def get_head_node(self):

					return self.head_node

				def push(self, arg):

					new_node = AstroNet().Sphere().HiveCell_f1(arg.value, arg.info)

					new_node.link_node = self.head_node

					self.head_node = new_node

				def HiveCell_f1_1(self, arg):

					counter=0

					var_set = set({})

					current_node = self.head_node

					while (counter!=arg):

						current_node = current_node.link_node

						print("Item", current_node)

						counter+=1

						print("Value", current_node.value)

					var_set.add(current_node)

					return var_set


				def add_conn_between_nodes_star_model(self):

					current_node = self.get_head_node()

					next_node = current_node.get_link_node()

					current_node.set_link_node(next_node.get_link_node())

					current_node.link_node2 = next_node

					inst_3 = next_node.get_link_node()

					next_node.set_link_node(next_node.get_link_node().get_link_node())

					print(str(current_node.info) +  " : "  + str(current_node.get_link_node().info))

					print(str(next_node.info) + " : " + str(next_node.get_link_node().info))

					next_node.link_node2 = inst_3

					next_node.set_link_node(next_node.get_link_node())  

					inst_3.link_node2 = inst_3.get_link_node()

					inst_f = inst_3.link_node2

					inst_3.set_link_node(next_node.get_link_node().get_link_node()) 

					print(str(inst_3.info)+ " : " + str(inst_3.get_link_node().info))#str(next_node.get_link_node().get_link_node()))

					inst_f.link_node2 = inst_f.get_link_node()

					inst_fl3 = inst_f.link_node2

					inst_fl2 = inst_f.link_node2.get_link_node()

					inst_f.set_link_node(inst_3.get_link_node().get_link_node())

					print(str(inst_f.info) + " : " + str(inst_f.get_link_node().info))

					inst_fl1 = inst_fl2.get_link_node()

					inst_fl3.set_link_node(inst_fl2)

					inst_fl3.link_node2 = inst_fl2

					inst_fl2.link_node2 = inst_fl1

					inst_fl1.set_link_node(None)

					print(str(inst_fl3.info)+ " : " + str(inst_fl3.get_link_node().info))

					print(str(inst_fl2.info) + " : " + str(inst_fl2.get_link_node().info))



					print("Printing the links to one node...")

					print(str(current_node.link_node2.info))
					print(str(next_node.link_node2.info))
					print(str(inst_3.link_node2.info))
					print(str(inst_f.link_node2.info))
					print(str(inst_fl3.link_node2.info))
					print(str(inst_fl2.link_node2.info))


					return self






		def The_Hive_main_function(self, the_hive_message="the_hive message"):

			class The_Hive(AstroNet.Sphere):

				def __init__(self):

					AstroNet.Sphere.__init__(self)

					self.the_hive_message = the_hive_message

				def the_Hive_f1(self):

					node1=AstroNet().Sphere().HiveCell_f1(1,"1st level");     node6=AstroNet().Sphere().HiveCell_f1(6, "3rd level");       node11=AstroNet().Sphere().HiveCell_f1(11, "4th level");
					node2=AstroNet().Sphere().HiveCell_f1(2,"1st level");     node7=AstroNet().Sphere().HiveCell_f1(7, "3rd level");       node12=AstroNet().Sphere().HiveCell_f1(12, "4th level");
					node3=AstroNet().Sphere().HiveCell_f1(3,"2nd level");	  node8=AstroNet().Sphere().HiveCell_f1(8, "3rd level");       node13=AstroNet().Sphere().HiveCell_f1(13, "4th level");
					node4=AstroNet().Sphere().HiveCell_f1(4, "2nd level");	  node9=AstroNet().Sphere().HiveCell_f1(9, "4th level");       node14=AstroNet().Sphere().HiveCell_f1(14, "4th level");
					node5=AstroNet().Sphere().HiveCell_f1(5, "3rd level");	  node10=AstroNet().Sphere().HiveCell_f1(10, "4th level");     node15=AstroNet().Sphere().HiveCell_f1(15,"5th level");

					node16=AstroNet().Sphere().HiveCell_f1(16, "5th level");  node21=AstroNet().Sphere().HiveCell_f1(21, "5th level");     node26=AstroNet().Sphere().HiveCell_f1(26, "Core level");
					node17=AstroNet().Sphere().HiveCell_f1(17, "5th level");  node22=AstroNet().Sphere().HiveCell_f1(22, "5th level");     node27=AstroNet().Sphere().HiveCell_f1(27, "Core level");
					node18=AstroNet().Sphere().HiveCell_f1(18, "5th level");  node23=AstroNet().Sphere().HiveCell_f1(23, "Core level");    node28=AstroNet().Sphere().HiveCell_f1(28, "Core level");
					node19=AstroNet().Sphere().HiveCell_f1(19, "5th level");  node24=AstroNet().Sphere().HiveCell_f1(24, "Core level");    node29=AstroNet().Sphere().HiveCell_f1(29, "Core level");
					node20=AstroNet().Sphere().HiveCell_f1(20, "5th level");  node25=AstroNet().Sphere().HiveCell_f1(25, "Core level");    node30=AstroNet().Sphere().HiveCell_f1(30, "Core level");

					node31=AstroNet().Sphere().HiveCell_f1(31, "Core level"); node36=AstroNet().Sphere().HiveCell_f1(36, "7th level");     node41=AstroNet().Sphere().HiveCell_f1(41, "8th level");
					node32=AstroNet().Sphere().HiveCell_f1(32, "Core level"); node37=AstroNet().Sphere().HiveCell_f1(37, "7th level");     node42=AstroNet().Sphere().HiveCell_f1(42, "8th level");
					node33=AstroNet().Sphere().HiveCell_f1(33, "7th level");  node38=AstroNet().Sphere().HiveCell_f1(38, "7th level");     node43=AstroNet().Sphere().HiveCell_f1(43, "8th level");
					node34=AstroNet().Sphere().HiveCell_f1(34, "7th level");  node39=AstroNet().Sphere().HiveCell_f1(39, "7th level");     node44=AstroNet().Sphere().HiveCell_f1(44, "8th level"); 
					node35=AstroNet().Sphere().HiveCell_f1(35, "7th level");  node40=AstroNet().Sphere().HiveCell_f1(40, "7th level");     node45=AstroNet().Sphere().HiveCell_f1(45, "8th level"); 
					
					node46=AstroNet().Sphere().HiveCell_f1(46, "8th level");  node51=AstroNet().Sphere().HiveCell_f1(51, "10th level");    node56=AstroNet().Sphere().HiveCell_f1(56,"Hive 1");
					node47=AstroNet().Sphere().HiveCell_f1(47, "9th level");  node52=AstroNet().Sphere().HiveCell_f1(52, "10th level");    node57=AstroNet().Sphere().HiveCell_f1(57,"Hive 1");
					node48=AstroNet().Sphere().HiveCell_f1(48, "9th level");  node53=AstroNet().Sphere().HiveCell_f1(53, "11th level");    node58=AstroNet().Sphere().HiveCell_f1(58,"Hive 1");
					node49=AstroNet().Sphere().HiveCell_f1(49, "9th level");  node54=AstroNet().Sphere().HiveCell_f1(54, "11th level");    node59=AstroNet().Sphere().HiveCell_f1(59, "Hive 2");
					node50=AstroNet().Sphere().HiveCell_f1(50, "9th level");  node55=AstroNet().Sphere().HiveCell_f1(55,"Hive 1");         node60=AstroNet().Sphere().HiveCell_f1(60, "Hive 2");
					
					node61=AstroNet().Sphere().HiveCell_f1(61, "Hive 2");     node66=AstroNet().Sphere().HiveCell_f1(66, "Hive 3");        node71=AstroNet().Sphere().HiveCell_f1(71, "Hive 5");
					node62=AstroNet().Sphere().HiveCell_f1(62, "Hive 2");     node67=AstroNet().Sphere().HiveCell_f1(67, "Hive 4");        node72=AstroNet().Sphere().HiveCell_f1(72, "Hive 5");
					node63=AstroNet().Sphere().HiveCell_f1(63, "Hive 3");     node68=AstroNet().Sphere().HiveCell_f1(68, "Hive 4");        node73=AstroNet().Sphere().HiveCell_f1(73, "Hive 5");
					node64=AstroNet().Sphere().HiveCell_f1(64, "Hive 3");     node69=AstroNet().Sphere().HiveCell_f1(69,"Hive 4");         node74=AstroNet().Sphere().HiveCell_f1(74, "Hive 5");
					node65=AstroNet().Sphere().HiveCell_f1(65, "Hive 3");     node70=AstroNet().Sphere().HiveCell_f1(70, "Hive 4");        node75=AstroNet().Sphere().HiveCell_f1(75, "Hive 6");

					node76=AstroNet().Sphere().HiveCell_f1(76,"Hive 6");      node81=AstroNet().Sphere().HiveCell_f1(81, "Hive 7");        node86=AstroNet().Sphere().HiveCell_f1(86, "Hive 8");
					node77=AstroNet().Sphere().HiveCell_f1(77,"Hive 6");      node82=AstroNet().Sphere().HiveCell_f1(82, "Hive 7");        node87=AstroNet().Sphere().HiveCell_f1(87, "Hive 9");
					node78=AstroNet().Sphere().HiveCell_f1(78,"Hive 6");      node83=AstroNet().Sphere().HiveCell_f1(83, "Hive 8");        node88=AstroNet().Sphere().HiveCell_f1(88, "Hive 9");
					node79=AstroNet().Sphere().HiveCell_f1(79,"Hive 7");      node84=AstroNet().Sphere().HiveCell_f1(84, "Hive 8");        node89=AstroNet().Sphere().HiveCell_f1(89, "Hive 9");
					node80=AstroNet().Sphere().HiveCell_f1(80,"Hive 7");      node85=AstroNet().Sphere().HiveCell_f1(85, "Hive 8");        node90=AstroNet().Sphere().HiveCell_f1(90, "Hive 9");
					
					node91=AstroNet().Sphere().HiveCell_f1(91,"Hive 10");     node96=AstroNet().Sphere().HiveCell_f1(96, "Hive 11");       node101=AstroNet().Sphere().HiveCell_f1(101,"Hive 12");
					node92=AstroNet().Sphere().HiveCell_f1(92, "Hive 10");    node97=AstroNet().Sphere().HiveCell_f1(97, "Hive 11");       node102=AstroNet().Sphere().HiveCell_f1(102,"Hive 12");
					node93=AstroNet().Sphere().HiveCell_f1(93, "Hive 10");    node98=AstroNet().Sphere().HiveCell_f1(98,"Hive 11");        node103=AstroNet().Sphere().HiveCell_f1(103, "Hive 13");
					node94=AstroNet().Sphere().HiveCell_f1(94, "Hive 10");    node99=AstroNet().Sphere().HiveCell_f1(99,"Hive 12");        node104=AstroNet().Sphere().HiveCell_f1(104, "Hive 13");
					node95=AstroNet().Sphere().HiveCell_f1(95, "Hive 11");    node100=AstroNet().Sphere().HiveCell_f1(100,"Hive 12");      node105=AstroNet().Sphere().HiveCell_f1(105, "Hive 13");

					node106=AstroNet().Sphere().HiveCell_f1(106, "Hive 13");  node111=AstroNet().Sphere().HiveCell_f1(111, "Hive 15");     node116=AstroNet().Sphere().HiveCell_f1(116, "Hive 16");
					node107=AstroNet().Sphere().HiveCell_f1(107, "Hive 14");  node112=AstroNet().Sphere().HiveCell_f1(112, "Hive 15");     node117=AstroNet().Sphere().HiveCell_f1(117, "Hive 16");
					node108=AstroNet().Sphere().HiveCell_f1(108, "Hive 14");  node113=AstroNet().Sphere().HiveCell_f1(113,"Hive 15");      node118=AstroNet().Sphere().HiveCell_f1(118, "Hive 16");
					node109=AstroNet().Sphere().HiveCell_f1(109, "Hive 14");  node114=AstroNet().Sphere().HiveCell_f1(114, "Hive 15");     node119=AstroNet().Sphere().HiveCell_f1(119, "Hive 17");
					node110=AstroNet().Sphere().HiveCell_f1(110, "Hive 14");  node115=AstroNet().Sphere().HiveCell_f1(115, "Hive 16");     node120=AstroNet().Sphere().HiveCell_f1(120,"Hive 17");

					node121=AstroNet().Sphere().HiveCell_f1(121,"Hive 17");   node126=AstroNet().Sphere().HiveCell_f1(126, "Hive 18");     node131=AstroNet().Sphere().HiveCell_f1(131, "Hive 20");
					node122=AstroNet().Sphere().HiveCell_f1(122,"Hive17");    node127=AstroNet().Sphere().HiveCell_f1(127, "Hive 19");     node132=AstroNet().Sphere().HiveCell_f1(132, "Hive 20");
					node123=AstroNet().Sphere().HiveCell_f1(123,"Hive 18");   node128=AstroNet().Sphere().HiveCell_f1(128, "Hive 19");     node133=AstroNet().Sphere().HiveCell_f1(133, "Hive 20");
					node124=AstroNet().Sphere().HiveCell_f1(124,"Hive 18");   node129=AstroNet().Sphere().HiveCell_f1(129, "Hive 19");     node134=AstroNet().Sphere().HiveCell_f1(134, "Hive 20");
					node125=AstroNet().Sphere().HiveCell_f1(125, "Hive 18");  node130=AstroNet().Sphere().HiveCell_f1(130, "Hive 19");     node135=AstroNet().Sphere().HiveCell_f1(135,"Hive 21");
					
					node136=AstroNet().Sphere().HiveCell_f1(136, "Hive 21");  node141=AstroNet().Sphere().HiveCell_f1(141, "Hive 22");
					node137=AstroNet().Sphere().HiveCell_f1(137, "Hive 21");  node142=AstroNet().Sphere().HiveCell_f1(142,"Hive 22");	
					node138=AstroNet().Sphere().HiveCell_f1(138, "Hive 21");
					node139=AstroNet().Sphere().HiveCell_f1(139, "Hive 22");
					node140=AstroNet().Sphere().HiveCell_f1(140, "Hive 22");


					the_Hive = AstroNet().Sphere().LinkedList(node1.value, node1.info)

					the_Hive.push(node2);   the_Hive.push(node3);   the_Hive.push(node4);   the_Hive.push(node5);   the_Hive.push(node6);   the_Hive.push(node7);
					the_Hive.push(node8);   the_Hive.push(node9);   the_Hive.push(node10);  the_Hive.push(node11);  the_Hive.push(node12);  the_Hive.push(node13);
					the_Hive.push(node14);  the_Hive.push(node15);  the_Hive.push(node16);  the_Hive.push(node17);  the_Hive.push(node18);  the_Hive.push(node19);
					the_Hive.push(node20);  the_Hive.push(node21);  the_Hive.push(node22);  the_Hive.push(node23);  the_Hive.push(node24);  the_Hive.push(node25);
					the_Hive.push(node26);  the_Hive.push(node27);  the_Hive.push(node28);  the_Hive.push(node29);  the_Hive.push(node30);  the_Hive.push(node31);
					the_Hive.push(node32);  the_Hive.push(node33);  the_Hive.push(node34);  the_Hive.push(node35);  the_Hive.push(node36);  the_Hive.push(node37);
					the_Hive.push(node38);  the_Hive.push(node39);  the_Hive.push(node40);  the_Hive.push(node41);  the_Hive.push(node42);  the_Hive.push(node43);
					the_Hive.push(node44);  the_Hive.push(node45);  the_Hive.push(node46);  the_Hive.push(node47);  the_Hive.push(node48);  the_Hive.push(node49);
					the_Hive.push(node50);  the_Hive.push(node51);  the_Hive.push(node52);  the_Hive.push(node53);  the_Hive.push(node54);


					node1.set_link_node1(node3);   node3.set_link_node1(node6);   node5.set_link_node1(node9);     node9.set_link_node1(node15);
					node2.set_link_node2(node4);   node3.set_link_node2(node5);   node5.set_link_node2(node10);    node10.set_link_node2(node16);
					node1.set_link_node3(node2);   node4.set_link_node3(node7);   node6.set_link_node3(node10);    node10.set_link_node3(node17);
					node1.set_link_node4(node2);   node4.set_link_node4(node8);   node6.set_link_node4(node11);    node11.set_link_node4(node18);
					node1.set_link_node5(node55);  node3.set_link_node5(node4);   node7.set_link_node5(node12);    node12.set_link_node5(node19);
					node1.set_link_node6(node102); node3.set_link_node6(node4);   node7.set_link_node6(node13);    node13.set_link_node6(node20);
					print("To 1st level");	       node3.set_link_node7(node59);  node8.set_link_node7(node13);    node13.set_link_node7(node21);
					print("To 1st level");	       node3.set_link_node8(node106); node8.set_link_node8(node14);    node14.set_link_node8(node22);
					print("To 1st level");	       print("To 2nd level");	      node6.set_link_node9(node5);     node9.set_link_node9(node10);
					print("To 1st level");	       print("To 2nd level");	      node5.set_link_node10(node6);    node10.set_link_node10(node9);
					print("To 1st level");	       print("To 2nd level");	      node8.set_link_node11(node7);    node10.set_link_node11(node11);
					print("To 1st level");	       print("To 2nd level");	      node7.set_link_node12(node8);    node11.set_link_node12(node10);
					print("To 1st level");	       print("To 2nd level");	      node5.set_link_node13(node7);    node12.set_link_node13(node13);
					print("To 1st level");	       print("To 2nd level");	      node6.set_link_node14(node8);    node13.set_link_node14(node12);
					print("To 1st level");	       print("To 2nd level");	      node5.set_link_node15(node63);   node13.set_link_node15(node14);
					print("To 1st level");	       print("To 2nd level");	      node6.set_link_node16(node110);  node14.set_link_node16(node13);
					print("To 1st level");	       print("To 2nd level");	      print("To 3rd level");	       node9.set_link_node17(node12);
					print("To 1st level");	       print("To 2nd level");	      print("To 3rd level");	       node11.set_link_node18(node14);
					print("To 1st level");	       print("To 2nd level");	      print("To 3rd level");	       node9.set_link_node19(node67);
					print("To 1st level");	       print("To 2nd level");	      print("To 3rd level");	       node11.set_link_node20(node11);


					node15.set_link_node1(node23);   node23.set_link_node1(node33);  node33.set_link_node1(node41);   node41.set_link_node1(node47);
					node16.set_link_node2(node24);   node24.set_link_node2(node34);  node34.set_link_node2(node42);   node42.set_link_node2(node47);
					node16.set_link_node4(node25);   node25.set_link_node4(node34);  node35.set_link_node4(node42);   node42.set_link_node4(node48);
					node17.set_link_node3(node25);   node25.set_link_node3(node35);  node36.set_link_node3(node43);   node43.set_link_node3(node48);
					node17.set_link_node5(node26);   node26.set_link_node5(node35);  node37.set_link_node5(node44);   node44.set_link_node5(node49);
					node18.set_link_node6(node27);   node27.set_link_node6(node36);  node38.set_link_node6(node45);   node45.set_link_node6(node49);
					node19.set_link_node7(node28);   node24.set_link_node7(node23);  node38.set_link_node6(node45);   node45.set_link_node7(node50);
					node20.set_link_node8(node29);   node23.set_link_node8(node24);  node39.set_link_node7(node45);   node46.set_link_node8(node50);
					node20.set_link_node9(node30);   node24.set_link_node9(node25);  node40.set_link_node8(node46);   node41.set_link_node9(node42);
					node21.set_link_node10(node30);  node25.set_link_node10(node24); node33.set_link_node9(node34);   node42.set_link_node10(node41);
					node21.set_link_node11(node31);  node25.set_link_node11(node26); node34.set_link_node10(node33);  node42.set_link_node11(node43);
					node22.set_link_node12(node32);  node26.set_link_node12(node25); node34.set_link_node11(node35);  node43.set_link_node12(node42);
					node15.set_link_node13(node16);  node26.set_link_node13(node27); node35.set_link_node12(node34);  node44.set_link_node13(node45);
					node16.set_link_node14(node15);  node27.set_link_node14(node26); node35.set_link_node13(node36);  node45.set_link_node14(node44);
					node16.set_link_node15(node17);  node28.set_link_node15(node29); node36.set_link_node14(node35);  node45.set_link_node15(node46);
					node17.set_link_node16(node16);  node29.set_link_node16(node28); node37.set_link_node15(node38);  node46.set_link_node16(node45);
					node17.set_link_node17(node18);  node29.set_link_node17(node30); node38.set_link_node16(node37);  node41.set_link_node17(node44);
					node18.set_link_node18(node17);  node30.set_link_node18(node29); node38.set_link_node17(node39);  node43.set_link_node18(node46);
					node19.set_link_node19(node20);  node30.set_link_node19(node31); node39.set_link_node18(node38);  node41.set_link_node19(node83);
					node20.set_link_node20(node19);  node31.set_link_node20(node30); node39.set_link_node19(node40);  node43.set_link_node20(node130);
					node20.set_link_node21(node21);  node31.set_link_node21(node32); node40.set_link_node20(node39);  print("To 8th level");
					node21.set_link_node22(node20);  node32.set_link_node22(node31); node33.set_link_node21(node37);  print("To 8th level");
					node21.set_link_node23(node22);  node28.set_link_node23(node37); node36.set_link_node22(node40);  print("To 8th level");
					node22.set_link_node24(node21);  node29.set_link_node24(node38); node33.set_link_node23(node79);  print("To 8th level");
					node15.set_link_node25(node19);  node30.set_link_node25(node38); node36.set_link_node24(node126); print("To 8th level");
					node18.set_link_node26(node22);  node30.set_link_node26(node39); print("To 7th level");           print("To 8th level");
					node15.set_link_node27(node71);  node31.set_link_node27(node39); print("To 7th level");           print("To 8th level");
					node18.set_link_node28(node118); node32.set_link_node28(node40); print("To 7th level");           print("To 8th level");
					print("To 5th level");           node23.set_link_node29(node28); print("To 7th level");           print("To 8th level");
					print("To 5th level");           node27.set_link_node30(node32); print("To 7th level");           print("To 8th level");
					print("To 5th level");	         node23.set_link_node31(node75); print("To 7th level");           print("To 8th level");
					print("To 5th level");           node27.set_link_node32(node122);print("To 7th level");           print("To 8th level");

					
					node47.set_link_node1(node51);  node51.set_link_node1(node53); node53.set_link_node1(node54);
					node48.set_link_node2(node51);  node52.set_link_node2(node54); node53.set_link_node2(node54);
					node49.set_link_node4(node52);  node51.set_link_node3(node52); node53.set_link_node3(node95);
					node50.set_link_node3(node52);  node51.set_link_node4(node52); node53.set_link_node4(node142);
					node47.set_link_node5(node48);  node51.set_link_node5(node91); print("To 11th level");
					node48.set_link_node6(node47);  node51.set_link_node6(node138);print("To 11th level");
					node49.set_link_node7(node50);  print("To 10th level");        print("To 11th level");
					node50.set_link_node8(node49);  print("To 10th level");        print("To 11th level");
					node47.set_link_node9(node49);  print("To 10th level");        print("To 11th level");
					node48.set_link_node10(node50); print("To 10th level");        print("To 11th level");
					node47.set_link_node11(node87); print("To 10th level");        print("To 11th level");
					node48.set_link_node12(node134);print("To 10th level");        print("To 11th level");

					return the_Hive

			var_the_Hive = The_Hive()

			return var_the_Hive

				
				
		class Account(Data):



			def __init__(self, name,  date_of_birth, country, friends, account_link1=1, account_link2=2, #value=1, info="data",
							bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"):

				self.profile = {'name':name, 'date_of_birth':date_of_birth, "country":country}
				self.friends = [friends]
				self.settings = {'private_profile':False, 'receive_messages':True, 'receive_emails':True}
				self.session = None #{active:yes}

				self.account_link1 = account_link1;
				self.account_link2 = account_link2; 

				self.bridge1 = bridge1
				self.bridge2 = bridge2
				self.bridge3 = bridge3
				self.bridge4 = bridge4
				self.bridge5 = bridge5
				self.bridge6 = bridge6
				self.bridge7 = bridge7
				self.bridge8 = bridge8
				self.bridge9 = bridge9
				self.bridge10 = bridge10
				self.bridge11 = bridge11
				self.bridge12 = bridge12
				self.bridge15 = bridge15
				self.bridge17 = bridge17
				self.bridge25 = bridge25
				self.bridge27 = bridge27

				self.account_message = account_message

				self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
											"Builder", "First", "First_message", "NestCell"]
				self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]

				super(AstroNet.Sphere.Account,self).__init__()




			def build_profile(self, name, date_of_birth, country):

				self.profile['name'] = name
				self.profile['date_of_birth'] = date_of_birth
				self.profile['country'] = country

				print(self.profile['name'])




			def edit_settings(self, name, date_of_birth, country, friends, settings_link1=1, settings_link2=2, settings_message="Settings message"):


				class Settings(AstroNet.Sphere.Account):

					settings_var = {'private_profile':False, 'receive_messages':True, 'receive_emails':True}


					def __init__(self): 

						self.settings = Settings.settings_var 

						AstroNet.Sphere.Account.__init__(self, name, date_of_birth, country, friends)

						self.settings_link1 = settings_link1;
						
						self.settings_link2 = settings_link2;

						self.settings_message = settings_message


					def edit_privacy_settings(self, arg):

						Settings.settings_var['private_profile'] = arg

						AstroNet.Sphere.Account.settings = self.settings = Settings.settings_var

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

			def __init__(self, person_link1=1, person_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6,
					 bridge7=7,bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
					bridge17=17, bridge25=25, bridge27=27, person_message="Person message"):

				self.centralized_database = [[[]for i in range(5)] for m in range(5)]

				self.person_link1 = person_link1
				self.person_link2 = person_link2

				self.bridge1 = bridge1
				self.bridge2 = bridge2
				self.bridge3 = bridge3
				self.bridge4 = bridge4
				self.bridge5 = bridge5
				self.bridge6 = bridge6
				self.bridge7 = bridge7
				self.bridge8 = bridge8
				self.bridge9 = bridge9
				self.bridge10 = bridge10
				self.bridge11 = bridge11
				self.bridge12 = bridge12
				self.bridge15 = bridge15
				self.bridge17 = bridge17
				self.bridge25 = bridge25
				self.bridge27 = bridge27

				self.person_message = person_message

				self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
											"Builder", "First", "First_message", "NestCell"]
				self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]





			def centralized_database_f1(self):

				return self.centralized_database

			def add_person_to_centralized_database(self, arg1):

				counter = 0

				for item in range(len(self.centralized_database)):

					print(item)

					print(self.centralized_database[item])

					for item1 in range(len(self.centralized_database[item])):

						print(item1)

						if self.centralized_database[item][item1] == []:


							if counter == 1:

								break

							
							counter+=1

							self.centralized_database[item][item1] = arg1

						print(counter)

				return self.centralized_database




		class Message(Account, Data):

			def __init__(self, arg1, title, message_content, message_link1=1, message_link2=2, message="Message"): #value=1, info="data",

				self.friends = arg1.friends

				self.messages = [ [dict({})] for item in range(len(arg1.friends))]

				self.message_text = {'Title':title, 'Message_content':message_content}

				self.message_link1 = message_link1;

				self.message_link2 = message_link2;

				super(AstroNet.Sphere.Message,self).__init__(name=arg1.profile['name'], date_of_birth=arg1.profile['date_of_birth'], country=arg1.profile['country'], friends=arg1.friends) 

				self.message = message

				super(AstroNet.Sphere.Message,self).__init__(name=arg1.profile['name'], date_of_birth=arg1.profile['date_of_birth'], country=arg1.profile['country'], friends=arg1.friends)



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

			def __init__(self, name, date_of_birth, country, friends, friend_link1=1, friend_link2=2, friend_message="Friend message"):

				super(AstroNet.Sphere.Friend,self).__init__(name, date_of_birth, country, friends) 

				self.friend_link1 = friend_link1;

				self.friend_link2 = friend_link2;

				self.friend_message = friend_message

				print(self.friends)



			def add_friends_from_the_same_network(self, name, date_of_birth, country, friends, friends_network_message="Friends network message"):

					#class which calls another class which calls another class

					#using specific attributes from the initial class

					class Friends_network(AstroNet.Sphere.Friend):


						def __init__(self, friends_network_link1=1, friends_network_link2=2):
							
							AstroNet.Sphere.Friend.__init__(self, name, date_of_birth, country, friends)

							self.friends_network_link1 = friends_network_link1;

							self.friends_network_link2 = friends_network_link2;

							self.friends_network_message = friends_network_message

							self.friends.append(self.profile['name'])

							for item in self.friends:

								print (item)



						def display_friends_list(self):

							return self.friends


					

					friends_network = Friends_network()

					return friends_network



				

			def add_friends(self, name, date_of_birth, country, friends, friends_network_message="Friends network message"):

				class Friends_network(AstroNet.Sphere.Friend):


					def __init__(self, friends_network_link1=1, friends_network_link2=2, ):

						#print(self.friends)

						#to access self.friends from the Friend class
						
						AstroNet.Sphere.Friend.__init__(self, name, date_of_birth, country, friends)

						self.friends_network_link1 = friends_network_link1;

						self.friends_network_link2 = friends_network_link2;

						self.friends_network_message = friends_network_message

						#the attributes of Friend are accessed through the Account class

						print(self.profile['name'])

						self.friends.append(name)

						#self.friends.append(self.profile['name'])

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





		class Session(Account):
			def __init__(self, user, session_link1=1, session_link2=2, session_message="Session message"):

				self.user = user

				self.active = user.session

				self.session_link1 = session_link1
				self.session_link2 = session_link2

				self.session_message = session_message

				super(AstroNet.Sphere.Session,self).__init__(name=user.profile['name'], date_of_birth=user.profile['date_of_birth'], country=user.profile['country'], friends=user.friends) 


			def display_user_status(self):

				if ((self.active==None) or (self.active==False)):

					print(self.user.profile['name'] + " is not logged in")


		  
		class AdjVertex():

			def __init__(self, data, adjVertex_link1=1, adjVertex_link2=2,bridge1=1,bridge2=2, 
						bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, adjVertex_message="AdjVertex message"):

				self.vertex = data
				self.next = None
				self.adjVertex_link1 = adjVertex_link1;
				self.adjVertex_link2 = adjVertex_link2;

				self.bridge1 = bridge1
				self.bridge2 = bridge2
				self.bridge3 = bridge3
				self.bridge4 = bridge4
				self.bridge5 = bridge5
				self.bridge6 = bridge6
				self.bridge7 = bridge7
				self.bridge8 = bridge8
				self.bridge9 = bridge9
				self.bridge10 = bridge10
				self.bridge11 = bridge11
				self.bridge12 = bridge12
				self.bridge15 = bridge15
				self.bridge17 = bridge17
				self.bridge25 = bridge25
				self.bridge27 = bridge27

				self.adjVertex_message = adjVertex_message

				self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
											"Builder", "First", "First_message", "NestCell"]
				self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]

		    


		class Graph():

			def __init__(self, vertices, graph_link1=1, graph_link2=2, bridge1=1,bridge2=2, 
						bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, graph_message="Graph message"):

				self.V = vertices
				self.graph = [None] * self.V
				self.graph_link1 = graph_link1;
				self.graph_link2 = graph_link2;

				self.bridge1 = bridge1
				self.bridge2 = bridge2
				self.bridge3 = bridge3
				self.bridge4 = bridge4
				self.bridge5 = bridge5
				self.bridge6 = bridge6
				self.bridge7 = bridge7
				self.bridge8 = bridge8
				self.bridge9 = bridge9
				self.bridge10 = bridge10
				self.bridge11 = bridge11
				self.bridge12 = bridge12
				self.bridge15 = bridge15
				self.bridge17 = bridge17
				self.bridge25 = bridge25
				self.bridge27 = bridge27

				self.graph_message = graph_message



				self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
											"Builder", "First", "First_message", "NestCell"]
				self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]


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

			def __init__(self, cell=7, shell=77, medium=777, link1=1, link2=2, link5=5, link7=7, builder_link1=1, builder_link2=2,
						bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, builder_message="Builder message"):

				self.counter=0

				self.network = {}

				self.level_counter = 0

				self.builder_link1=builder_link1;

				self.builder_link2 = builder_link2;

				self.bridge1 = bridge1
				self.bridge2 = bridge2
				self.bridge3 = bridge3
				self.bridge4 = bridge4
				self.bridge5 = bridge5
				self.bridge6 = bridge6
				self.bridge7 = bridge7
				self.bridge8 = bridge8
				self.bridge9 = bridge9
				self.bridge10 = bridge10
				self.bridge11 = bridge11
				self.bridge12 = bridge12
				self.bridge15 = bridge15
				self.bridge17 = bridge17
				self.bridge25 = bridge25
				self.bridge27 = bridge27

				self.builder_message = builder_message

				self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
											"Builder", "First", "First_message", "NestCell"]
				self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]


			
			def build_the_friend_network_f1_A(self, arg1, arg2, arg3, arg5):

				print("1st call")

				arg1.friends = arg1.add_friends_from_the_same_network(arg2, arg3, arg5, arg1.friends).friends

				return arg1.add_friends_from_the_same_network(arg1, arg2, arg5, arg1.friends).friends



			def build_the_friend_network_f1_1_A(self, arg1, arg2, arg3, arg5):

				print("1st call")

				arg1.friends = arg1.add_friends_from_the_same_network(arg2, arg3, arg5, arg1.friends).friends

				return arg1.add_friends_from_the_same_network(arg1, arg2, arg5, arg1.friends).friends



			def build_the_friend_network_f1_B(self, arg1, arg2, arg3, arg5):

				print("1st call")

				arg1.friends = arg1.add_friends(arg2, arg3, arg5, arg1.friends).friends

				return arg1.add_friends(arg1, arg2, arg5, arg1.friends).friends



			def instance_f1(self,arg1, arg2, arg3, arg5, arg6, arg7):

				#self.counter += 1

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


			def create_a_vertex_list(self, arg1):

				var_vertex_list = []

				var_vertex_list.append(arg1[1])

				for item in arg1[1].__dict__['friends']:

					if type(item) ==  list:

						for item1 in item:

							print("Value", item1)

							var_vertex_list.append(item1)


					if type(item) != list:

						print("Value1:", item.__dict__)

						var_vertex_list.append(item)



				return var_vertex_list





			def create_a_vertex_list_f1(self, arg1):

				var_vertex_list = []

				var_vertex_list1 = []

				var_vertex_list.append(arg1[1])

				for item in arg1[1].__dict__['friends']:

					if type(item) ==  list:

						for item1 in item:

							print("Value", item1)

							var_vertex_list.append(item1)


					if type(item) != list:

						print("Value1:", item.__dict__)

						var_vertex_list.append(item)


				#var_vertex_list1.append(arg1[1])

				for i in var_vertex_list:

					if type(i) == AstroNet.Sphere.AdjVertex:

						print("Vertex", i.__dict__)

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

					print("conn", args_list[0].next)

					print("conn1", args_list[0].next.__dict__)

					var_graph_list.append(args_list[0].next)

					#var_graph.build_graph(args_list[0].next)

					var_graph.graph = var_graph_list

				#var_graph.add_edge_f1_2(var_graph, args_list[0], args_list[1])

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

					print("****Item****:", item)
					print("****Item****:", item.__dict__)


					for item1 in  arg1.create_a_vertex_list_f1(arg5):

						print("****item1****", item1)
						print("****Item1****:", item1.__dict__)


						if item.__dict__['vertex']['name'] == item1.__dict__['vertex']['name']:

							print()

							print("^^^^^^^^^^^^^^^^^^^^Item^^^^^^^^^^^^^^^^^^^^", (item.__dict__))

							args_list.append(item)

				var_graph = AstroNet().Sphere().Graph(len(args_list))

				#print("Graph")

				print("Var graph", type(var_graph))

				for item in range(len(args_list)):

				    print("***********Arg*************:", args_list[item].__dict__)

				    var_graph.add_edge_f1_2(var_graph, args_list[0], args_list[item])

				    print("conn", args_list[0].next)

				    print("conn1", args_list[0].next.__dict__)

				    var_graph_list.append(args_list[0].next)

				    var_graph.build_graph(args_list[0].next)

				    #var_graph.graph = var_graph_list


				#var_graph.add_edge_f1_2(var_graph, args_list[0], args_list[1])

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

								print("Friends list1: ", friend)

								var_initial_level.append(("Second level", friend))

						elif 'friends' in item.__dict__:

							for friend in item.__dict__['friends']:

								print("Friends list1_1: ", friend)

								var_initial_level.append(("Second level", friend))


					else: 

						for item1 in item:

							if type(item1) != list:

								print("Third", item1.__dict__)

								var_initial_level.append(("Third level:", item1))

								# for friend1 in item1.__dict__['friends']:

								# 	print("Friends list2: ", friend1)


								if ('vertex' in item1.__dict__ and 'friends' in item1.__dict__['vertex'] 
								and 'friends' not in item1.__dict__):

									print("******")
											
									for friend1 in item1.__dict__['vertex']['friends']:

										print("Friends list2: ", friend1)

										var_friends_of_friends.append(friend1)

										var_initial_level.append(("Third level", friend1))

								if ('vertex' in item1.__dict__ and 'friends' in item1.__dict__['vertex'] 
								and 'friends' in item1.__dict__):

									print("*************")

									print("Len:", len(item1.__dict__['friends']))

									for friend1 in item1.__dict__['friends']:

										if type(friend1) != list:

											print("*******************")

											print("Friends list2:", friend1.__dict__)

											var_friends_of_friends.append(friend1)

											var_initial_level.append(("Third level", friend1))


										else:

											pass


											
						
				print("var_initial_level", var_initial_level)

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


			def __init__(self, name, date_of_birth, country, friends, first_link1=1, first_link2=2, first_friend_message="First friend message"):

				#the attributes from the __init__ method of account are inherited

				super(AstroNet.Sphere.First,self).__init__(name, date_of_birth, country, friends) 

				self.first_link1 = first_link1;

				self.first_link2 = first_link2;

				self.first_friend_message = first_friend_message

				print("**********************************************************")

				print(self.friends)

				print("***********************************************************")


			def add_friends_from_the_same_network(self, name, date_of_birth, country, friends, arg1, arg2,  friends_network_message="Friends_network message"):

				    print("----------------------------------------------------")

					#check if the arguments match the data of the friends from the same network

				    class Friends_network(AstroNet.Sphere.Friend):

			    		 def __init__(self, friends_network_link1=1, friends_network_link2=2):

			    		 	AstroNet.Sphere.Friend.__init__(self, name, date_of_birth, country, friends) #arg1,arg2)

			    		 	self.friends_network_link1 = friends_network_link1;

			    		 	self.friends_network_link2 = friends_network_link2;

			    		 	self.friends_network_message = friends_network_message

			    		    #the attributes of Friend are accessed through the Account class


			    		 	self.f1 = AstroNet.Sphere.Builder.f1


			    		 	if self.f1(self, arg1, arg2, self.profile['name']):

			    		 		self.friends.append(self.profile['name'])

			    		 		print("Friends list 7: ", self.friends)

			    		 		for item in self.friends:

			    		 			print("Item 7:", item)

					
				    friends_network = Friends_network()

				    return friends_network




		class First_message(Account):

			def __init__(self, arg1, title, message_content, first_message_link1=1, first_message_link2=2, first_message="First message"):

				self.friends = arg1.friends

				self.messages = [[dict({})] for item in range(len(arg1.friends))]

				self.message_text = {'Title':title, 'Message_content':message_content}

				self.first_message_link1 = first_message_link1;

				self.first_message_link2 = first_message_link2;

				super(AstroNet.Sphere.First_message,self).__init__(name=arg1.profile['name'], date_of_birth=arg1.profile['date_of_birth'], country=arg1.profile['country'], friends=arg1.friends) 

				self.first_message = first_message

				print(self.friends)

				print(self.messages)

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

							 		print("Found: ", item1)

							 		print(1)
							 		return item1

						 	else:

						 		pass

			def send_message_to_a_friend_from_the_same_network(self, arg1, arg2):

				counter = 0

				if (arg2 in arg1.friends):

					counter+=1

					#arg2=counter

					self.messages.append(self.message_text)

				else:

					print(arg2 + " is not a member of your friends network.")
					answer =input("Would you like to add " + arg2 + " to your friends network? Type yes or no ")

					print("True")

					if (answer == "yes"):

						arg1.add_friends(arg2, "1992, 7, 7", "NL", "Q")

						print(arg2 + " is now your friend ")


				return self.messages


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

						self.messages.append(self.message_text)


				print("Messages: ", self.messages)

				print("Friends: ", friends_list)



				return (self.messages, arg1)





		class NestCell(Builder):


			def __init__(self, cell, shell, medium, link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message"):

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

				self.nest_cell_message = nest_cell_message

				

			class Gate1():

				def __init__(self, gate1_link1=1, gate1_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate1_message="Gate1 message"):

					self.gate1_link1 = gate1_link1;

					self.gate1_link2 = gate1_link2;

					self.bridge1 = bridge1
					self.bridge2 = bridge2
					self.bridge3 = bridge3
					self.bridge4 = bridge4
					self.bridge5 = bridge5
					self.bridge6 = bridge6
					self.bridge7 = bridge7
					self.bridge8 = bridge8
					self.bridge9 = bridge9
					self.bridge10 = bridge10
					self.bridge11 = bridge11
					self.bridge12 = bridge12
					self.bridge15 = bridge15
					self.bridge17 = bridge17
					self.bridge25 = bridge25
					self.bridge27 = bridge27

					self.gate1_message = gate1_message

					self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
												"Builder", "First", "First_message", "NestCell"]
					self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]




				def build_the_nest_cell(self, cell, shell, medium, link1=1, link2=2, link5=5, link7=7, nesting_hive_message="NestingHive message"):

					class NestingHive(AstroNet.Sphere.NestCell):

						def __init__(self, nestingHive_link1=1, nestingHive_link2=2, ):

							#to access 

							AstroNet.Sphere.NestCell.__init__(self, cell, shell, medium)

							self.nestingHive_link1 = nestingHive_link1;

							self.nestingHive_link2 = nestingHive_link2;

							self.nesting_hive_message = nesting_hive_message

							
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

					#return self.network

					the_hive = NestingHive()

					return the_hive

			
			class Gate2():

				def __init__(self, gate2_link1=1, gate2_link2=2, bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate2_message="Gate2 message"):

					self.gate2_link1 = gate2_link1;

					self.gate2_link2 = gate2_link2;

					self.bridge1 = bridge1
					self.bridge2 = bridge2
					self.bridge3 = bridge3
					self.bridge4 = bridge4
					self.bridge5 = bridge5
					self.bridge6 = bridge6
					self.bridge7 = bridge7
					self.bridge8 = bridge8
					self.bridge9 = bridge9
					self.bridge10 = bridge10
					self.bridge11 = bridge11
					self.bridge12 = bridge12
					self.bridge15 = bridge15
					self.bridge17 = bridge17
					self.bridge25 = bridge25
					self.bridge27 = bridge27

					self.gate2_message = gate2_message

					self.primary_memory = ["LinkedList","Account", "Session", "Person", "Message", "Friend", "AdjVertex", "Graph",
												"Builder", "First", "First_message", "NestCell"]
					self.secondary_memory=["HiveCell", "TheHive", "Settings", "Friends_network", "Gate1", "NestingHive", "Gate2"]



				def path_function(self, cell, shell, medium, link1=1, link2=2, link5=5, link7=7):

					return AstroNet().Sphere().NestCell(cell, shell, medium).Gate1().build_the_nest_cell(self, cell, shell, medium).canal()


		def connect(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10,arg11, arg12, arg15, arg17, arg25, arg27):

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
			self.link27 = arg27

			return self

		def create_map(self, arg1, arg2, arg3, arg4, arg5, arg7, arg8, arg10, arg11, arg12, arg15, arg17, arg25, arg27, arg35, arg37):

			arg1.account_link1 = arg2
			arg2.session_link1 = arg3
			arg3.settings_link1 = arg4
			arg4.message_link1=arg5
			arg5.first_message_link1 = arg7
			arg7.friend_link1 = arg8
			arg8.friends_network_link1 = arg10
			arg10.adjVertex_link1 = arg11
			arg11.graph_link1 = arg12
			arg12.builder_link1 = arg15
			arg15.person_link1 = arg17
			arg17.first_link1 = arg25
			arg25.nestCell_link1 = arg27
			arg27.gate1_link1 = arg35
			arg35.nestingHive_link1 = arg37
			arg37.gate2_link1 = arg1

			arg2.session_link2 = arg1
			arg3.settings_link2 = arg2
			arg4.message_link2 = arg3
			arg5.first_message_link2 = arg4
			arg7.friend_link2 = arg5
			arg8.friends_network_link2 = arg7
			arg10.adjVertex_link2 = arg8
			arg11.graph_link2 = arg10
			arg12.builder_link2 = arg11
			arg15.person_link2 = arg12
			arg17.first_link2 = arg15
			arg25.nestCell_link2 = arg17
			arg27.gate1_link2 = arg25
			arg35.nestingHive_link2 = arg27
			arg37.gate2_link2 = arg1

			return self




		def build_bridges(self, arg, arg1, arg2, arg3, arg4, arg5,arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg15, arg17, arg25):

			arg.bridge1 = arg1
			arg.bridge2 = arg2
			arg.bridge3 = arg3
			arg.bridge4 = arg4
			arg.bridge5 = arg5
			arg.bridge6 = arg6
			arg.bridge7 = arg7
			arg.bridge8 = arg8
			arg.bridge9 = arg9
			arg.bridge10 = arg10
			arg.bridge11 = arg11
			arg.bridge12 = arg12
			arg.bridge15 = arg15
			arg.bridge17 = arg17
			arg.bridge25 = arg25

			return arg

		

		def send_message_f1(self, arg1, arg2):

			counter = 0

			counter1 = 0

			var_path = ['account_message', 'session_message','settings_message','person_message','message', 
						'friend_message','friends_network_message','adjVertex_message', 'graph_message',
						'builder_message','first_friend_message','first_message','nest_cell_message', 
						'gate1_message','nesting_hive_message','gate2_message']

			for item in var_path:

				if item in arg1.__dict__:

					counter+=1

					print(item)

					var_message = item

					print("Counter", counter)


			for item1 in var_path:

				counter1+=1

				if item1 in arg2.__dict__:

					print(item1)

					var_message1 = item1

					print("Counter1", counter1)

					counter2=counter1

			print(var_message, var_message1)

			print(arg2.__dict__[var_message1])

			arg2.__dict__[var_message1] = arg1.__dict__[var_message]

			print(arg2.__dict__[var_message1])

			var_path1 = []

			print(counter2)


			for item in range(counter2):

				print(item)

				var_path1.append(var_path[item])

			print(var_path1)


			return((arg1, arg2), var_path1)


		def send_message_using_the_map_f1(self, arg1, arg2):
			
			var_directed_path = self.send_message_f1(arg1, arg2)

			print(var_directed_path[0])

			print(var_directed_path[1])	

			var_path = ['hive_cell_message','linked_list_message', 'the_hive_message','account_message', 'session_message','settings_message','person_message','message', 
						'friend_message','friends_network_message','adjVertex_message', 'graph_message',
						'builder_message','first_friend_message','first_message','nest_cell_message', 
						'gate1_message','nesting_hive_message','gate2_message']

			var_directed_path1 = [

							AstroNet().Sphere().HiveCell_f1(),

							AstroNet().Sphere().LinkedList(value=1, info="data"),

							AstroNet().Sphere().The_Hive_main_function(),

							AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", #value=1, info="data",
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"),

							 AstroNet().Sphere().Session(user=AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"),

							 	session_link1=1, session_link2=2, session_message="Session message"),

							 AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message").edit_settings(name="name", date_of_birth="date_of_birth", country="country", friends="friends", settings_link1=1, settings_link2=2, settings_message="Settings message"),


							 AstroNet().Sphere().Person(person_link1=1, person_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6,
							 bridge7=7,bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							 bridge17=17, bridge25=25, bridge27=27, person_message="Person message"),

							 AstroNet().Sphere().Message(arg1=AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"), title="title", message_content="message_content", message_link1=1, message_link2=2, message="Message"), 
							
							AstroNet().Sphere().Friend(name="name", date_of_birth="date_of_birth", country="country", friends="friends", friend_link1=1, friend_link2=2, friend_message="Friend message"),


							AstroNet().Sphere().Friend(name="name", date_of_birth="date_of_birth", country="country", friends="friends", friend_link1=1, friend_link2=2, friend_message="Friend message").add_friends(name="name", date_of_birth="date_of_birth", country="country", friends="friends", friends_network_message="Friends network message"),

							AstroNet().Sphere().AdjVertex( data=1, adjVertex_link1=1, adjVertex_link2=2,bridge1=1,bridge2=2, 
						bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, adjVertex_message="AdjVertex message"), 

							AstroNet().Sphere().Graph(vertices=1, graph_link1=1, graph_link2=2, bridge1=1,bridge2=2, 
						bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, graph_message="Graph message"),

							AstroNet().Sphere().Builder(cell=7, shell=77, medium=777, link1=1, link2=2, link5=5, link7=7, builder_link1=1, builder_link2=2,
						bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, builder_message="Builder message"),
							
							AstroNet().Sphere().First(name="name", date_of_birth="date_of_birth", country="country", friends="friends", first_link1=1, first_link2=2, first_friend_message="First friend message"),

							AstroNet().Sphere().First_message(arg1=AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"), title="title", message_content="message_content", first_message_link1=1, first_message_link2=2, first_message="First message"),

							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message"),

							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message").Gate1(gate1_link1=1, gate1_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate1_message="Gate1 message"),


							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message").Gate1(gate1_link1=1, gate1_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate1_message="Gate1 message").build_the_nest_cell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nesting_hive_message="NestingHive message"),


							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message").Gate2(gate2_link1=1, gate2_link2=2, bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate2_message="Gate2 message")]

			var_directed_path2 = []

			for item in range(len(var_directed_path[1])):

				#print(var_directed_path1[item].__dict__[var_directed_path[1][item]])

				var_directed_path1[item].__dict__[var_directed_path[1][item]] = var_directed_path[1][0]

				print(var_directed_path1[item].__dict__[var_directed_path[1][item]])

				var_directed_path2.append(var_directed_path1[item])

			AstroNet().Sphere().create_map(var_directed_path1[0], var_directed_path1[1],var_directed_path1[2],var_directed_path1[3],
				var_directed_path1[4], var_directed_path1[5],var_directed_path1[6],var_directed_path1[7], var_directed_path1[8], 
				var_directed_path1[9], var_directed_path1[10],var_directed_path1[11],var_directed_path1[12], 
				var_directed_path1[13], var_directed_path1[14],
				var_directed_path1[15])
			


			return (var_directed_path1, var_directed_path2)


		def send_message_using_bridges_f1(self, arg1, arg2):

			var_list = AstroNet().Sphere().send_message_using_the_map_f1(arg1, arg2)

			AstroNet().Sphere().build_bridges(var_list[1][0], var_list[0][1], var_list[0][2],
				var_list[0][3], var_list[0][4], var_list[0][5], var_list[0][6], var_list[0][7],
				var_list[0][8], var_list[0][9], var_list[0][10], var_list[0][11], 
				var_list[0][12], var_list[0][13], var_list[0][14], var_list[0][15])

			return var_list


		def send_message_using_the_star_model(self, arg1, arg2):

			var_directed_path = self.send_message_f1(arg1, arg2)

			print(var_directed_path[1])

			item_list = []

			item_list1 = []

			set_var_primary = set({})

			set_var_secondary = set({})



			for item in range(len(var_directed_path[1])):

				# for item1 in arg1.primary_memory:

					# if (var_directed_path[1][item].split("_").join(" ").find(item1)):

					# 	print("item", var_directed_path[1][item].find(item1))

					#print(var_directed_path[1][item].split("_"))

					item_list.append(var_directed_path[1][item].split("_"))

			for item1 in range(len(item_list)):

				print("list", item_list[item1])

			for item in range(len(item_list)):

				for item1 in item_list[item]:

					print(item1)

					item_list1.append(item1)

			print(item_list1)

			for item in item_list1:

				for item1 in arg1.primary_memory:

					if item.upper() in item1.upper():

						print("Item", item)
						print("Item1", item1)

						set_var_primary.add(item1)

				for item1 in arg1.secondary_memory:

					if item.upper() in item1.upper():

						set_var_secondary.add(item1)



			print(set_var_primary)
			print(set_var_secondary)

			return (set_var_primary, set_var_secondary)



		def send_message_using_the_star_model_f1(self, arg1, arg2):

			var_path = ['hive_cell_message','linked_list_message', 'the_hive_message','account_message', 'session_message','settings_message','person_message','message', 
						'friend_message','friends_network_message','adjVertex_message', 'graph_message',
						'builder_message','first_friend_message','first_message','nest_cell_message', 
						'gate1_message','nesting_hive_message','gate2_message']

			var_directed_path = self.send_message_f1(arg1, arg2)

			print(var_directed_path[1])	

			star_model = self.send_message_using_the_star_model(arg1, arg2)

			list1 = [item for item in star_model[0]]

			list2 = [item for item in star_model[1]]

			var_list = list1 + list2

			print(var_list)



			var_directed_path1 = [

							AstroNet().Sphere().HiveCell_f1(),

							AstroNet().Sphere().LinkedList(value=1, info="data"),

							AstroNet().Sphere().The_Hive_main_function(),

							AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", #value=1, info="data",
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"),

							 AstroNet().Sphere().Session(user=AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"),

							 	session_link1=1, session_link2=2, session_message="Session message"),

							 AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message").edit_settings(name="name", date_of_birth="date_of_birth", country="country", friends="friends", settings_link1=1, settings_link2=2, settings_message="Settings message"),


							 AstroNet().Sphere().Person(person_link1=1, person_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6,
							 bridge7=7,bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							 bridge17=17, bridge25=25, bridge27=27, person_message="Person message"),

							 AstroNet().Sphere().Message(arg1=AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"), title="title", message_content="message_content", message_link1=1, message_link2=2, message="Message"), 
							
							AstroNet().Sphere().Friend(name="name", date_of_birth="date_of_birth", country="country", friends="friends", friend_link1=1, friend_link2=2, friend_message="Friend message"),


							AstroNet().Sphere().Friend(name="name", date_of_birth="date_of_birth", country="country", friends="friends", friend_link1=1, friend_link2=2, friend_message="Friend message").add_friends(name="name", date_of_birth="date_of_birth", country="country", friends="friends", friends_network_message="Friends network message"),

							AstroNet().Sphere().AdjVertex( data=1, adjVertex_link1=1, adjVertex_link2=2,bridge1=1,bridge2=2, 
						bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, adjVertex_message="AdjVertex message"), 

							AstroNet().Sphere().Graph(vertices=1, graph_link1=1, graph_link2=2, bridge1=1,bridge2=2, 
						bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, graph_message="Graph message"),

							AstroNet().Sphere().Builder(cell=7, shell=77, medium=777, link1=1, link2=2, link5=5, link7=7, builder_link1=1, builder_link2=2,
						bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,bridge8=8,bridge9=9, bridge10=10, 
						bridge11=11, bridge12=12, bridge15=15,bridge17=17, bridge25=25, bridge27=27, builder_message="Builder message"),
							
							AstroNet().Sphere().First(name="name", date_of_birth="date_of_birth", country="country", friends="friends", first_link1=1, first_link2=2, first_friend_message="First friend message"),

							AstroNet().Sphere().First_message(arg1=AstroNet().Sphere().Account(name="name", date_of_birth="date of birth", country="country", friends="friends", 
							account_link1=1, account_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15,
							bridge17=17, bridge25=25, bridge27=27, account_message="Account message"), title="title", message_content="message_content", first_message_link1=1, first_message_link2=2, first_message="First message"),

							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message"),

							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message").Gate1(gate1_link1=1, gate1_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate1_message="Gate1 message"),


							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message").Gate1(gate1_link1=1, gate1_link2=2,bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate1_message="Gate1 message").build_the_nest_cell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nesting_hive_message="NestingHive message"),


							AstroNet().Sphere().NestCell(cell="cell", shell="shell", medium="medium", link1=1, link2=2, link5=5, link7=7, nestCell_link1=1, nestCell_link2=2, nest_cell_message="NestCell message").Gate2(gate2_link1=1, gate2_link2=2, bridge1=1,bridge2=2, bridge3=3, bridge4=4, bridge5=5, bridge6=6, bridge7=7,
							bridge8=8,bridge9=9, bridge10=10, bridge11=11, bridge12=12, bridge15=15, bridge17=17, bridge25=25, bridge27=27, gate2_message="Gate2 message")]

			print(var_directed_path1[1].linked_list_message)

			print(var_directed_path[1])

			print(var_list)


			items_set = set({})
			items_set1 = set({})

			for item in var_path:

				for item1 in var_directed_path1:

					for obj in item1.__dict__:

						if obj == item:

							print("obj", obj)

							items_set.add(obj)

			print(items_set)

			for item in var_list:

				for item1 in var_directed_path1:

					for obj in item1.__dict__:

						if item.upper() + "_" + "message".upper() == obj.upper():

							print("obj", obj)

							items_set1.add(obj)

						if item.upper() == obj.upper():

							print("obj", obj)

							items_set1.add(obj)

			list_items_set1 = []

			for item in items_set1 :

				list_items_set1.append(item)

			print("list_items_set1", list_items_set1)


			for item1 in  list_items_set1:

				if (("_" not in item1) and (item1 != "message") and  (item1 != "first_message")):

					list_items_set1.remove(item1)
			print("list_items_set1", list_items_set1)

			items_set1 = list_items_set1

			print("items_set", items_set)
			print()

			print("items_set1", items_set1)
			print()

			print(var_list)

			linked_list = AstroNet().Sphere().LinkedList(arg1.value, arg1.info)

			
			set1 = set({})

			for name in var_list:
				for item in items_set1:

					for item1 in  range(len(var_directed_path1)):

						if (name in str(var_directed_path1[item1].__class__)):

							for obj in var_directed_path1[item1].__dict__:

								if obj == item:

									print("Found", obj)

									set1.add(var_directed_path1[item1])

			print(set1)


			print(len(set1))

			linked_list = AstroNet().Sphere().LinkedList(arg1.value, arg1.info)

			# for item1 in list(set1):

			for item in var_list:

				item = AstroNet().Sphere().HiveCell_f1(info=item)#, instance=item1)

				print("instance", item.instance)

				linked_list.push(item)


			print(linked_list.head_node.info)

			print(linked_list.head_node.link_node.info)


			current_node = linked_list.head_node

			print("Current_node:",current_node)

			print("Current_node.value", current_node.value)

			print("Current_node.info", current_node.info)


			print("Vertex", current_node.info)

			print("Vertex", current_node.link_node.info)

			print("Vertex", current_node.link_node.link_node.info)

			print("Vertex", current_node.link_node.link_node.link_node.info)

			print("Vertex", current_node.link_node.link_node.link_node.link_node.info)

			print("Vertex", current_node.link_node.link_node.link_node.link_node.link_node.info)

			print("Vertex", current_node.link_node.link_node.link_node.link_node.link_node.link_node.info)





			for item1 in list(set1):

				while current_node:

					current_node = current_node.link_node

					current_node.instance = item1

					print("Instance",current_node.instance)


					break

			print("Instance", current_node.instance)

			if len(star_model[1]) <= len(arg1.secondary_memory):

				linked_list.add_conn_between_nodes_star_model()

			current_node = linked_list.head_node

			print("Vertex1", current_node.info)

			print("Vertex1", current_node.link_node.info)

			print("Vertex1", current_node.link_node.link_node.info)

			print("Vertex1", current_node.link_node.link_node.link_node.info)

			print("Vertex1", current_node.link_node.link_node.link_node.link_node.info)

			#print("Vertex1", current_node.link_node.link_node.link_node.link_node.link_node.info)

			#print("Vertex1", current_node.link_node.link_node.link_node.link_node.link_node.link_node.info)


			print(len(var_list))

			return linked_list

			


		def retrieve_data_from_the_hive(self, arg):

			print(self.The_Hive_main_function())

			# print(self.The_Hive_main_function().the_Hive_f1().head_node.value)

			# print(self.The_Hive_main_function().the_Hive_f1().head_node.link_node.value)

			var = self.The_Hive_main_function().the_Hive_f1().HiveCell_f1_1(arg)

			for item in var:

				var1 = (item.value, item.info)

			return var1


		def create_list_for_sending_message(self, arg):

			self.communications_list = arg

			return self.communications_list

		def send_message_using_the_map_f2(self, arg1, arg2, arg3):

			var = self.send_message_using_the_map_f1(arg1, arg2)

			var_items =[]

			for item in var[0]:

				var_items.append(item)

			print(var_items)

			for i in range(len(var_items)):

				for item in range(len(arg3)):

					if type(var_items[i]) == type(arg3[item]):

						#print(var_items[i])

						print(var[0][i])

						var[0][i] = arg3[item]

			return var


		def send_message_using_bridges_f2(self, arg1, arg2, arg3):


			var = self.send_message_using_bridges_f1(arg1, arg2)

			var_items =[]

			for item in var[0]:

				var_items.append(item)

			print(var_items)

			for i in range(len(var_items)):

				for item in range(len(arg3)):

					if type(var_items[i]) == type(arg3[item]):

						#print(var_items[i])

						print(var[0][i])

						var[0][i] = arg3[item]

			return var


		def send_message_using_the_star_model_f2(self, arg1, arg2, arg3):

			var = self.send_message_using_the_star_model_f1(arg1, arg2)

			print(var)

			current_node = var.head_node
		
			
			while current_node:

				current_node = current_node.link_node

				#print(current_node)

				for item in arg3:

					print(item)

					if current_node:

						print("item", current_node.instance)

						print(current_node)

						if ((type(current_node.instance) == type(item))):

							print("Found", current_node.instance)

							current_node.instance = item

			return var

						
		class Point():
			def __init__(self, value):
				self.point = value

			def __str__(self):
				return str(self.point)


		class Line():
			def __init__(self, p1, p2):
				self.line = [p1, p2]

			def __str__(self):
				return str(self.line)

			def line_edges(self):

				point1 = str(self.line[0])
				point2 = str(self.line[1])
				line = [point1, point2]

				return line

			def print_line_edges(self):

				point1 = str(self.line[0])
				point2 = str(self.line[1])
				line = [point1, point2]

				print(line)

			

		class Polyhedron():

			def __init__(self):
				self.polyhedron = []
				self.first_level_connections_list = []
				self.second_level_connections_list = []
				self.third_level_connections_list = []
				self.facets = []

			def __str__(self):

				return str(self.polyhedron)
			

			def build_first_level_connections_list(self, p1):

				self.first_level_connections_list.append(p1)

				return self.first_level_connections_list
			

			def first_level_connections_list(self):

				first_level_connections = []

				for item in self.first_level_connections_list: 

					line_edges = item.line_edges()
					
					first_level_connections.append(line_edges)
				
				return first_level_connections


			def print_first_level_connections_list(self):

				first_level_connections = []

				for item in self.first_level_connections_list: 

					line_edges = item.line_edges()
					
					first_level_connections.append(line_edges)
					
				print(first_level_connections)

				
			def build_second_level_connections_list(self, p1):

				self.second_level_connections_list.append(p1)

				return self.second_level_connections_list

			
			def second_level_connections_list(self):

				second_level_connections = []

				for item in self.second_level_connections_list: 

					line_edges = item.line_edges()
					
					second_level_connections.append(line_edges)
				
				return second_level_connections


			def print_second_level_connections_list(self):

				second_level_connections = []

				for item in self.second_level_connections_list: 

					line_edges = item.line_edges()
					
					second_level_connections.append(line_edges)
					
				print(second_level_connections)


			def build_third_level_connections_list(self, p1):

				self.third_level_connections_list.append(p1)

				return self.third_level_connections_list

			def third_level_connections_list(self):

				third_level_connections = []

				for item in self.third_level_connections_list: 

					line_edges = item.line_edges()
					
					third_level_connections.append(line_edges)
				
				return third_level_connections


			def print_third_level_connections_list(self):

				third_level_connections = []

				for item in self.third_level_connections_list: 

					line_edges = item.line_edges()
					
					third_level_connections.append(line_edges)
					
				print(third_level_connections)




			


AstroNet.Sphere.AdjVertex.add_friends_from_the_same_network = AstroNet.Sphere.Friend.add_friends_from_the_same_network

AstroNet.Sphere.AdjVertex.builder_function = AstroNet.Sphere.Builder.builder_function

AstroNet.Sphere.AdjVertex.friends = []

AstroNet.Sphere.AdjVertex.add_friends = AstroNet.Sphere.Friend.add_friends

AstroNet.Sphere.AdjVertex.builder_function_1 = AstroNet.Sphere.Builder.builder_function_1

AstroNet.Sphere.AdjVertex.builder_function_2 = AstroNet.Sphere.Builder.builder_function_2

AstroNet.Sphere.AdjVertex.builder_function_5 = AstroNet.Sphere.Builder.builder_function_5




AstroNet.Sphere.First.add_friends = AstroNet.Sphere.Friend.add_friends

AstroNet.Sphere.First.add_yourself_to_the_list_of_friends = AstroNet.Sphere.Friend.add_yourself_to_the_list_of_friends

AstroNet.Sphere.Message.send_message_to_a_friend_from_the_same_network = AstroNet.Sphere.First_message.send_message_to_a_friend_from_the_same_network_f1






varA = AstroNet().Sphere().Point('A'); varAPrime = AstroNet().Sphere().Point('A\'')
varB = AstroNet().Sphere().Point('B'); varBPrime = AstroNet().Sphere().Point('B\'')
varC = AstroNet().Sphere().Point('C'); varCPrime = AstroNet().Sphere().Point('C\'')
varD = AstroNet().Sphere().Point('D'); varDPrime = AstroNet().Sphere().Point('D\'')
varE = AstroNet().Sphere().Point('E'); varEPrime = AstroNet().Sphere().Point('E\'')
varF = AstroNet().Sphere().Point('F'); varFPrime = AstroNet().Sphere().Point('F\'')
varG = AstroNet().Sphere().Point('G'); varGPrime = AstroNet().Sphere().Point('G\'')
varH = AstroNet().Sphere().Point('H'); varHPrime = AstroNet().Sphere().Point('H\'')


varI = AstroNet().Sphere().Point('I'); varIPrime = AstroNet().Sphere().Point('I\'')
varJ = AstroNet().Sphere().Point('J'); varJPrime = AstroNet().Sphere().Point('J\'')
varK = AstroNet().Sphere().Point('K'); varKPrime = AstroNet().Sphere().Point('K\'')
varL = AstroNet().Sphere().Point('L'); varLPrime = AstroNet().Sphere().Point('L\'')
varM = AstroNet().Sphere().Point('M'); varMPrime = AstroNet().Sphere().Point('M\'')
varN = AstroNet().Sphere().Point('N'); varNPrime = AstroNet().Sphere().Point('N\'')
varO = AstroNet().Sphere().Point('O'); varOPrime = AstroNet().Sphere().Point('O\'')
varP = AstroNet().Sphere().Point('P'); varPPrime = AstroNet().Sphere().Point('P\'')


varQ = AstroNet().Sphere().Point('Q'); varQPrime = AstroNet().Sphere().Point('Q\'')
varR = AstroNet().Sphere().Point('R'); varRPrime = AstroNet().Sphere().Point('R\'')
varS = AstroNet().Sphere().Point('S'); varSPrime = AstroNet().Sphere().Point('S\'')
varT = AstroNet().Sphere().Point('T'); varTPrime = AstroNet().Sphere().Point('T\'')
varU = AstroNet().Sphere().Point('U'); varUPrime = AstroNet().Sphere().Point('U\'')
varV = AstroNet().Sphere().Point('V'); varVPrime = AstroNet().Sphere().Point('V\'')
varW = AstroNet().Sphere().Point('W'); varWPrime = AstroNet().Sphere().Point('W\'')
varX = AstroNet().Sphere().Point('X'); varXPrime = AstroNet().Sphere().Point('X\''); 


varY = AstroNet().Sphere().Point('Y'); varYPrime = AstroNet().Sphere().Point('Y\''); 

# print(varA)
# print(varAPrime)


# two-dimensional

line1 = AstroNet().Sphere().Line(varA, varB); line45= AstroNet().Sphere().Line(varAPrime, varBPrime)
line2 = AstroNet().Sphere().Line(varB, varC); line46 = AstroNet().Sphere().Line(varBPrime, varCPrime)
line3 = AstroNet().Sphere().Line(varC, varD); line47 = AstroNet().Sphere().Line(varCPrime, varDPrime)
line4 = AstroNet().Sphere().Line(varD, varE); line48 = AstroNet().Sphere().Line(varDPrime, varEPrime)
line5 = AstroNet().Sphere().Line(varE, varF); line49 = AstroNet().Sphere().Line(varEPrime, varFPrime)
line6 = AstroNet().Sphere().Line(varF, varG); line50 = AstroNet().Sphere().Line(varFPrime, varGPrime)
line7 = AstroNet().Sphere().Line(varG, varH); line51 = AstroNet().Sphere().Line(varGPrime, varHPrime)
line8 = AstroNet().Sphere().Line(varH, varA); line52 = AstroNet().Sphere().Line(varHPrime, varAPrime)


line9 = AstroNet().Sphere().Line(varI, varJ);  line53 = AstroNet().Sphere().Line(varIPrime, varJPrime)
line10 = AstroNet().Sphere().Line(varJ, varK); line54 = AstroNet().Sphere().Line(varJPrime, varKPrime)
line11 = AstroNet().Sphere().Line(varK, varL); line55 = AstroNet().Sphere().Line(varKPrime, varLPrime)
line12 = AstroNet().Sphere().Line(varL, varM); line56 = AstroNet().Sphere().Line(varLPrime, varMPrime)
line13 = AstroNet().Sphere().Line(varM, varN); line57 = AstroNet().Sphere().Line(varMPrime, varNPrime)
line14 = AstroNet().Sphere().Line(varN, varO); line58 = AstroNet().Sphere().Line(varNPrime, varOPrime)
line15 = AstroNet().Sphere().Line(varO, varP); line59 = AstroNet().Sphere().Line(varOPrime, varPPrime)
line16 = AstroNet().Sphere().Line(varP, varI); line60 = AstroNet().Sphere().Line(varPPrime, varIPrime)


line17 = AstroNet().Sphere().Line(varQ, varR); line61 = AstroNet().Sphere().Line(varQPrime, varRPrime)
line18 = AstroNet().Sphere().Line(varR, varS); line62 = AstroNet().Sphere().Line(varRPrime, varSPrime)
line19 = AstroNet().Sphere().Line(varS, varT); line63 = AstroNet().Sphere().Line(varSPrime, varTPrime)
line20 = AstroNet().Sphere().Line(varT, varU); line64 = AstroNet().Sphere().Line(varTPrime, varUPrime)
line21 = AstroNet().Sphere().Line(varU, varV); line65 = AstroNet().Sphere().Line(varUPrime, varVPrime)
line22 = AstroNet().Sphere().Line(varV, varW); line66 = AstroNet().Sphere().Line(varVPrime, varWPrime)
line23 = AstroNet().Sphere().Line(varW, varX); line67 = AstroNet().Sphere().Line(varWPrime, varXPrime)
line24 = AstroNet().Sphere().Line(varX, varQ); line68 = AstroNet().Sphere().Line(varXPrime, varQPrime)


#3 dimensional

line25 = AstroNet().Sphere().Line(varA, varI); line70 = AstroNet().Sphere().Line(varAPrime, varIPrime)
line26 = AstroNet().Sphere().Line(varB, varJ); line71 = AstroNet().Sphere().Line(varBPrime, varJPrime)
line27 = AstroNet().Sphere().Line(varC, varK); line72 = AstroNet().Sphere().Line(varCPrime, varKPrime)
line28 = AstroNet().Sphere().Line(varD, varL); line73 = AstroNet().Sphere().Line(varDPrime, varLPrime)
line29 = AstroNet().Sphere().Line(varE, varU); line74 = AstroNet().Sphere().Line(varEPrime, varUPrime)
line30 = AstroNet().Sphere().Line(varF, varN); line75 = AstroNet().Sphere().Line(varFPrime, varNPrime)
line31 = AstroNet().Sphere().Line(varG, varO); line76 = AstroNet().Sphere().Line(varGPrime, varOPrime)
line32 = AstroNet().Sphere().Line(varH, varX); line77 = AstroNet().Sphere().Line(varHPrime, varXPrime)


line33 = AstroNet().Sphere().Line(varI, varQ); line78 = AstroNet().Sphere().Line(varIPrime, varQPrime)
line34 = AstroNet().Sphere().Line(varJ, varP); line79 = AstroNet().Sphere().Line(varJPrime, varPPrime)
line35 = AstroNet().Sphere().Line(varK, varS); line80 = AstroNet().Sphere().Line(varKPrime, varSPrime)
line36 = AstroNet().Sphere().Line(varL, varT); line81 = AstroNet().Sphere().Line(varLPrime, varTPrime)
line37 = AstroNet().Sphere().Line(varM, varU); line82 = AstroNet().Sphere().Line(varMPrime, varUPrime)
line38 = AstroNet().Sphere().Line(varN, varV); line83 = AstroNet().Sphere().Line(varNPrime, varVPrime)
line39 = AstroNet().Sphere().Line(varO, varW); line84 = AstroNet().Sphere().Line(varOPrime, varWPrime)
line40 = AstroNet().Sphere().Line(varP, varX); line85 = AstroNet().Sphere().Line(varPPrime, varXPrime)



line41 = AstroNet().Sphere().Line(varP, varY); line86 = AstroNet().Sphere().Line(varPPrime, varYPrime)
line42 = AstroNet().Sphere().Line(varT, varY); line87 = AstroNet().Sphere().Line(varTPrime, varYPrime)
line43 = AstroNet().Sphere().Line(varU, varY); line88 = AstroNet().Sphere().Line(varUPrime, varYPrime)
line44 = AstroNet().Sphere().Line(varV, varY); line89 = AstroNet().Sphere().Line(varVPrime, varYPrime)


# print(line1)
# line1.print_line_edges()


polyhedron1 = AstroNet().Sphere().Polyhedron()


# second dimension

polyhedron1.build_first_level_connections_list(line1); polyhedron1.build_first_level_connections_list(line45)
polyhedron1.build_first_level_connections_list(line2); polyhedron1.build_first_level_connections_list(line46)
polyhedron1.build_first_level_connections_list(line3); polyhedron1.build_first_level_connections_list(line47)
polyhedron1.build_first_level_connections_list(line4); polyhedron1.build_first_level_connections_list(line48)
polyhedron1.build_first_level_connections_list(line5); polyhedron1.build_first_level_connections_list(line49)
polyhedron1.build_first_level_connections_list(line6); polyhedron1.build_first_level_connections_list(line50)
polyhedron1.build_first_level_connections_list(line7); polyhedron1.build_first_level_connections_list(line51)
polyhedron1.build_first_level_connections_list(line8); polyhedron1.build_first_level_connections_list(line52)


# third dimension

polyhedron1.build_first_level_connections_list(line25); polyhedron1.build_first_level_connections_list(line70)
polyhedron1.build_first_level_connections_list(line26); polyhedron1.build_first_level_connections_list(line71)
polyhedron1.build_first_level_connections_list(line27); polyhedron1.build_first_level_connections_list(line72)
polyhedron1.build_first_level_connections_list(line28); polyhedron1.build_first_level_connections_list(line73)
polyhedron1.build_first_level_connections_list(line29); polyhedron1.build_first_level_connections_list(line74)
polyhedron1.build_first_level_connections_list(line30); polyhedron1.build_first_level_connections_list(line75)
polyhedron1.build_first_level_connections_list(line31); polyhedron1.build_first_level_connections_list(line76)
polyhedron1.build_first_level_connections_list(line32); polyhedron1.build_first_level_connections_list(line77)


polyhedron1.print_first_level_connections_list()


# second dimension

polyhedron1.build_second_level_connections_list(line9); polyhedron1.build_second_level_connections_list(line53)
polyhedron1.build_second_level_connections_list(line10); polyhedron1.build_second_level_connections_list(line54)
polyhedron1.build_second_level_connections_list(line11); polyhedron1.build_second_level_connections_list(line55)
polyhedron1.build_second_level_connections_list(line12); polyhedron1.build_second_level_connections_list(line56)
polyhedron1.build_second_level_connections_list(line13); polyhedron1.build_second_level_connections_list(line57)
polyhedron1.build_second_level_connections_list(line14); polyhedron1.build_second_level_connections_list(line58)
polyhedron1.build_second_level_connections_list(line15); polyhedron1.build_second_level_connections_list(line59)
polyhedron1.build_second_level_connections_list(line16); polyhedron1.build_second_level_connections_list(line60)


# third dimension

polyhedron1.build_second_level_connections_list(line33); polyhedron1.build_second_level_connections_list(line78)
polyhedron1.build_second_level_connections_list(line34); polyhedron1.build_second_level_connections_list(line79)
polyhedron1.build_second_level_connections_list(line35); polyhedron1.build_second_level_connections_list(line80)
polyhedron1.build_second_level_connections_list(line36); polyhedron1.build_second_level_connections_list(line81)
polyhedron1.build_second_level_connections_list(line37); polyhedron1.build_second_level_connections_list(line82)
polyhedron1.build_second_level_connections_list(line38); polyhedron1.build_second_level_connections_list(line83)
polyhedron1.build_second_level_connections_list(line39); polyhedron1.build_second_level_connections_list(line84)
polyhedron1.build_second_level_connections_list(line40); polyhedron1.build_second_level_connections_list(line85)

polyhedron1.print_second_level_connections_list()


#second dimension 

polyhedron1.build_third_level_connections_list(line17); polyhedron1.build_third_level_connections_list(line61)
polyhedron1.build_third_level_connections_list(line18); polyhedron1.build_third_level_connections_list(line62)
polyhedron1.build_third_level_connections_list(line19); polyhedron1.build_third_level_connections_list(line63)
polyhedron1.build_third_level_connections_list(line20); polyhedron1.build_third_level_connections_list(line64)
polyhedron1.build_third_level_connections_list(line21); polyhedron1.build_third_level_connections_list(line65)
polyhedron1.build_third_level_connections_list(line22); polyhedron1.build_third_level_connections_list(line66)
polyhedron1.build_third_level_connections_list(line23); polyhedron1.build_third_level_connections_list(line67)
polyhedron1.build_third_level_connections_list(line24); polyhedron1.build_third_level_connections_list(line68)


#third dimension

polyhedron1.build_third_level_connections_list(line41); polyhedron1.build_third_level_connections_list(line86)
polyhedron1.build_third_level_connections_list(line42); polyhedron1.build_third_level_connections_list(line87)
polyhedron1.build_third_level_connections_list(line43); polyhedron1.build_third_level_connections_list(line88)
polyhedron1.build_third_level_connections_list(line44); polyhedron1.build_third_level_connections_list(line89)


polyhedron1.print_third_level_connections_list()



