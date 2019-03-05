# Read into the excel file as input
# generate a series of xml file 
# call Nairnmpm to run the code

from lxml import etree

#Mesh_size = 

page = etree.Element('JANFEAInput',version='3')
doc = etree.ElementTree(page)

Header = etree.SubElement(page,'Header')
MPMHeader = etree.SubElement(page,'MPMHeader')
Mesh = etree.SubElement(page,'Mesh',output='file')
MaterialPoints = etree.SubElement(page,'MaterialPoints')
################ define the material parameters  ########################
Material1 = etree.SubElement(page,'Material', Type='101', Name = 'Sand')
etree.SubElement(Material1,'G').text = "0.323e6"
etree.SubElement(Material1,'nu').text = "0.3"
etree.SubElement(Material1,'rho').text = "2.65e3"
etree.SubElement(Material1,'Hardening').text = "DpHardening"
etree.SubElement(Material1,'q_fai').text = "0.239"
etree.SubElement(Material1,'k_fai').text = "0.12"
etree.SubElement(Material1,'q_psi').text = "0"
etree.SubElement(Material1,'sig_t').text = "0"

Material2 = etree.SubElement(page,'Material', Type='61', Name = 'Coulomb Friction')
etree.SubElement(Material2,'coeff').text = "0.4"
etree.SubElement(Material2,'coeffStatic').text = "0.4"

Material3 = etree.SubElement(page,'Material', Type='11', Name = 'Bottom')
etree.SubElement(Material3,'SetDirection').text = "8"
etree.SubElement(Material3,'mirrored').text = "1"
etree.SubElement(Material3,'Friction',law='2' ,mat='1')

Material4 = etree.SubElement(page,'Material', Type='11', Name = 'Side wall')
etree.SubElement(Material4,'SetDirection').text = "8"
etree.SubElement(Material4,'mirrored').text = "1"

Material5 = etree.SubElement(page,'Material', Type='1', Name = 'Barrier')
etree.SubElement(Material5,'E').text = "5e5"
etree.SubElement(Material5,'nu').text = "0.3"
etree.SubElement(Material5,'rho').text = "2.65e3"

Material6 = etree.SubElement(page,'Material', Type='11', Name = 'door')
etree.SubElement(Material6,'SetDirection').text = "8"
etree.SubElement(Material6,'mirrored').text = "1"
etree.SubElement(Material6,'SettingFunction').text='0'
etree.SubElement(Material6,'SettingFunction2').text='( sign(t-1.0)- sign(t-1.200) )*3.000'
etree.SubElement(Material6,'SettingFunction3').text='0'

#########################################################################
Gravity = etree.SubElement(page,'Gravity')
etree.SubElement(Gravity,'BodyXForce').text = "6.427876096865393"
etree.SubElement(Gravity,'BodyYForce').text = "-7.66044443118978"
etree.SubElement(Gravity,'BodyZForce').text = "0"

GridBCs = etree.SubElement(page,'GridBCs')
CustomTasks = etree.SubElement(page,'CustomTasks')

# start each SubElement of page
# Header
etree.SubElement(Header,'Description').text = "Description of the simulation"
etree.SubElement(Header,'ConsistentUnits', length='m', mass='kg',time='s')
etree.SubElement(Header,'Analysis').text ="12"
#MPMHeader
etree.SubElement(MPMHeader,'MPMMethod').text = "2"
etree.SubElement(MPMHeader,'GIMP', type='uGIMP')
etree.SubElement(MPMHeader,'TimeStep').text = "1e-3"
etree.SubElement(MPMHeader,'TimeFactor').text = "0.5"
etree.SubElement(MPMHeader,'MaxTime').text = "3"
etree.SubElement(MPMHeader,'ArchiveRoot').text = "Impact3D_40_Feb24_0.04mThick/impact"
etree.SubElement(MPMHeader,'ArchiveTime').text = "0.04"
etree.SubElement(MPMHeader,'MPMArchiveOrder').text = "iYYYYNNNNNNNYNNNNYNNN"
etree.SubElement(MPMHeader,'GlobalArchiveTime').text = "0.04"
etree.SubElement(MPMHeader,'GlobalArchive',type='sxx',material='3')
etree.SubElement(MPMHeader,'GlobalArchive',type='Kinetic Energy',material='3')
etree.SubElement(MPMHeader,'GlobalArchive',type='Work Energy',material='3')
etree.SubElement(MPMHeader,'GlobalArchive',type='sxx',material='1')
etree.SubElement(MPMHeader,'GlobalArchive',type='Kinetic Energy',material='1')
etree.SubElement(MPMHeader,'GlobalArchive',type='Work Energy',material='1')
etree.SubElement(MPMHeader,'GlobalArchive',type='Internal Energy',material='1')
etree.SubElement(MPMHeader,'GlobalArchive',type='Plastic Energy',material='1')
etree.SubElement(MPMHeader,'PDamping',PIC='0.01').text = "0.75"
MultiMaterialMode= etree.SubElement(MPMHeader,'MultiMaterialMode',Vmin='0.8',Dcheck='1',Normals='2',RigidBias='0')
etree.SubElement(MultiMaterialMode,'ContactPosition').text = "0.8"
etree.SubElement(MultiMaterialMode,'Friction', law='2')

#Mesh
Grid = etree.SubElement(Mesh,'Grid',xmin='-0.8',xmax='2', ymin='-0.2', ymax="1", zmin='-0.3', zmax='0.3')
etree.SubElement(Grid,'Horiz',nx='140')
etree.SubElement(Grid,'Vert',ny='60')
etree.SubElement(Grid,'Depth',nz='30')

#MaterialPoints
Body1 = etree.SubElement(MaterialPoints,'Body',mat='1', vx='0', vy='0', vz='0')
etree.SubElement(Body1,'Box',xmin='-0.18',xmax='0',ymin='0',ymax='0.315',zmin='-0.1',zmax='0.1')

Body2 = etree.SubElement(MaterialPoints,'Body',mat='3',vx='0',vy='0',vz='0')
etree.SubElement(Body2,'Box',xmin='-0.8',xmax='2',ymin='-0.2',ymax='0',zmin='-0.1',zmax='0.1')

Body3 = etree.SubElement(MaterialPoints,'Body',mat='4',vx='0', vy='0', vz='0')
etree.SubElement(Body3,'Box',xmin='-0.8',xmax='2',ymin='-0.2',ymax='1', zmin='-0.3',zmax='-0.1')
etree.SubElement(Body3,'Box',xmin='-0.8',xmax='2',ymin='-0.2',ymax='1', zmin='0.1',zmax='0.3')

Body4 = etree.SubElement(MaterialPoints,'Body',mat='4',vx='0', vy='0', vz='0')
etree.SubElement(Body4,'Box',xmin='-0.3',xmax='-0.2' ,ymin='0', ymax='0.8', zmin='-0.1', zmax='0.1')

Body5 = etree.SubElement(MaterialPoints,'Body',mat='3',vx='0', vy='0', vz='0')
etree.SubElement(Body5,'Box',xmin='1.2' ,xmax='1.24', ymin='0', ymax='0.6' ,zmin='-0.2' ,zmax='0.2')

Body6 = etree.SubElement(MaterialPoints,'Body',mat='6',vx='0', vy='0', vz='0')
etree.SubElement(Body6,'Box',xmin='0' ,xmax='0.2' ,ymin='0', ymax='0.6', zmin='-0.1', zmax='0.1')

#GridBCs
BC1 = etree.SubElement(GridBCs,'BCBox',xmin='-0.8',xmax='2',ymin='-0.2',ymax='-0.05',zmin='-0.2',zmax='0.2')
etree.SubElement(BC1,'DisBC',dir='1', style='constant', vel='0')
etree.SubElement(BC1,'DisBC',dir='2', style='constant', vel='0')
etree.SubElement(BC1,'DisBC',dir='3', style='constant', vel='0')

BC2 = etree.SubElement(GridBCs,'BCBox',xmin='1.2',xmax='1.24',ymin='-0.1',ymax='0.6',zmin='-0.2',zmax='-0.1')
etree.SubElement(BC2,'DisBC',dir='1', style='constant', vel='0')
etree.SubElement(BC2,'DisBC',dir='2', style='constant', vel='0')
etree.SubElement(BC2,'DisBC',dir='3', style='constant', vel='0')

BC3 = etree.SubElement(GridBCs,'BCBox',xmin='1.2',xmax='1.24',ymin='-0.1',ymax='0.6',zmin='0.1',zmax='0.2')
etree.SubElement(BC3,'DisBC',dir='1', style='constant', vel='0')
etree.SubElement(BC3,'DisBC',dir='2', style='constant', vel='0')
etree.SubElement(BC3,'DisBC',dir='3', style='constant', vel='0')

BC4 = etree.SubElement(GridBCs,'BCBox',xmin='-0.8',xmax='-0.25',ymin='0',ymax='1',zmin='-0.2',zmax='0.2')
etree.SubElement(BC4,'DisBC',dir='1', style='constant', vel='0')
etree.SubElement(BC4,'DisBC',dir='2', style='constant', vel='0')
etree.SubElement(BC4,'DisBC',dir='3', style='constant', vel='0')
#linkElt = etree.SubElement(headElt,'link',rel='stylesheet', href='mystyle.css',type ='text/css')

outFile = open('homemade.xml','w')
s = etree.tostring(doc, pretty_print=True)
outFile.write(s)
