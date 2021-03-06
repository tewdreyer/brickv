'''OpenGL extension ARB.draw_buffers_blend

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_draw_buffers_blend'
_DEPRECATED = False

glBlendEquationi = platform.createExtensionFunction( 
'glBlendEquationi',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,),
doc='glBlendEquationi(GLuint(buf), GLenum(mode)) -> None',
argNames=('buf','mode',),
deprecated=_DEPRECATED,
)

glBlendEquationSeparatei = platform.createExtensionFunction( 
'glBlendEquationSeparatei',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLenum,),
doc='glBlendEquationSeparatei(GLuint(buf), GLenum(modeRGB), GLenum(modeAlpha)) -> None',
argNames=('buf','modeRGB','modeAlpha',),
deprecated=_DEPRECATED,
)

glBlendFunci = platform.createExtensionFunction( 
'glBlendFunci',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLenum,),
doc='glBlendFunci(GLuint(buf), GLenum(src), GLenum(dst)) -> None',
argNames=('buf','src','dst',),
deprecated=_DEPRECATED,
)

glBlendFuncSeparatei = platform.createExtensionFunction( 
'glBlendFuncSeparatei',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLenum,constants.GLenum,constants.GLenum,),
doc='glBlendFuncSeparatei(GLuint(buf), GLenum(srcRGB), GLenum(dstRGB), GLenum(srcAlpha), GLenum(dstAlpha)) -> None',
argNames=('buf','srcRGB','dstRGB','srcAlpha','dstAlpha',),
deprecated=_DEPRECATED,
)


def glInitDrawBuffersBlendARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
