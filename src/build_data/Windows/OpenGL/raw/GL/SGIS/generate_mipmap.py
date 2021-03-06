'''OpenGL extension SGIS.generate_mipmap

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_generate_mipmap'
_DEPRECATED = False
GL_GENERATE_MIPMAP_SGIS = constant.Constant( 'GL_GENERATE_MIPMAP_SGIS', 0x8191 )
GL_GENERATE_MIPMAP_HINT_SGIS = constant.Constant( 'GL_GENERATE_MIPMAP_HINT_SGIS', 0x8192 )
glget.addGLGetConstant( GL_GENERATE_MIPMAP_HINT_SGIS, (1,) )


def glInitGenerateMipmapSGIS():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
